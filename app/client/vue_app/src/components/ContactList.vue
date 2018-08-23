<template>
  <div class="max-w-lg mx-auto h-screen bg-white px-8 pt-8 shadow-lg">
    <div class="flex">

      <ul class="contact-list">
        <li class="contact-list__contact" @click="editContact(contact)" v-for="contact in sortedContacts" :key="contact.id">
          <p> {{ contact.firstname }} {{ contact.lastname }} </p>
        </li>
        <button class="contact-list__add-contact-btn" @click="editNewContact">Add contact</button>
      </ul>

      <transition name="expand">
        <div class="contact-editor" v-if="selectedContact">
          <div class="contact-editor__data-section">
            <div class="flex-col">
              <input v-validate="'required|alpha|max:15'" name="firstname" class="contact-editor__input" placeholder="First name" v-model="selectedContact.firstname" />
              <p class="contact-editor__validation-error-msg">{{ errors.first('firstname') }}</p>
            </div>
            <div>
              <input v-validate="'required|alpha|max:15'" name="lastname" class="contact-editor__input" placeholder="Last name"  v-model="selectedContact.lastname" />
              <p class="contact-editor__validation-error-msg">{{ errors.first('lastname') }}</p>
            </div>
            <datepicker input-class="contact-editor__input" placeholder="birthdate" v-model="selectedContact.birthdate"></datepicker>
          </div>

          <div class="contact-editor__data-section">
            <h4>Addresses</h4>
            <div v-for="(address, index) in selectedContact.addresses" :key="`address-${index}`">
              <input v-validate="'required'" class="contact-editor__input" :name="`address[${index}]`" :placeholder="`Address ${index+1}`" v-model="selectedContact.addresses[index]" />
              <button class="contact-editor__btn contact-editor__btn--delete" @click="selectedContact.addresses.splice(index, 1)">delete</button>
              <p class="contact-editor__validation-error-msg">{{ errors.first(`address[${index}]`) }}</p>
            </div>
            <button class="contact-editor__btn contact-editor__btn--add-data" @click="addAddress">Add address</button>
          </div>

          <div class="contact-editor__data-section">
            <h4>Phone numbers</h4>
            <div v-for="(phoneNumber, index) in selectedContact.phone_numbers" :key="`phone-number-${index}`">
              <div class="flex">
                <input v-validate="'required|numeric|max:13'" class="contact-editor__input w-1/3 mr-1" :name="`phone_number[${index}]`" :placeholder="`Phone ${index+1}`" v-model="selectedContact.phone_numbers[index].phone_number" />
                <div class="relative w-1/3 mr-1">
                  <select class="contact-editor__phone-number__type-select" v-model="selectedContact.phone_numbers[index].phone_type">
                    <option>Personal</option>
                    <option>Work</option>
                    <option>Home</option>
                  </select>
                  <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                  </div>
                </div>
                <button class="contact-editor__btn contact-editor__btn--delete" v-if="phoneNumberCount > 1" @click="selectedContact.phone_numbers.splice(index, 1)">delete</button>
              </div>
              <p class="contact-editor__validation-error-msg">{{ errors.first(`phone_number[${index}]`) }}</p>
            </div>
            <button class="contact-editor__btn contact-editor__btn--add-data" @click="addPhoneNumber">Add phone</button>
          </div>

          <div class="contact-editor__data-section">
            <h4>Emails</h4>
            <div v-for="(email, index) in selectedContact.emails" :key="`email-${index}`">
              <div class="flex">
                <input v-validate="'required|email'" class="contact-editor__input" :name="`email[${index}]`" :placeholder="`Email ${index+1}`" v-model="selectedContact.emails[index]" />
                <button class="contact-editor__btn contact-editor__btn--delete" v-if="emailCount > 1" @click="selectedContact.emails.splice(index, 1)">delete</button>
              </div>
              <p class="contact-editor__validation-error-msg">{{ errors.first(`email[${index}]`) }}</p>
            </div>
            <button class="contact-editor__btn contact-editor__btn--add-data" @click="addEmail">Add Email</button>
          </div>

          <template v-if="editingNewContact">
            <button class="contact-editor__btn contact-editor__btn--save" @click="createContact">Create</button>
            <button class="contact-editor__btn contact-editor__btn--delete" @click="cancelEdit">Cancel</button>
          </template>
          <template v-else>
            <button class="contact-editor__btn contact-editor__btn--save" @click="updateContact">Update</button>
            <button class="contact-editor__btn contact-editor__btn--delete" @click="deleteContact">Delete</button>
          </template>

        </div>
      </transition>

    </div>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker'
import backend from '../backend'

export default {
  components: {
    Datepicker
  },
  created () {
    backend.getContacts()
      .then(({data}) => {
        this.contacts = data.contacts
      })
  },
  data () {
    return {
      contacts: [],
      selectedContact: null,
      editingNewContact: false
    }
  },
  methods: {
    editContact (contact) {
      this.$validator.reset()
      this.selectedContact = contact
      this.editingNewContact = false
    },
    addEmail () {
      this.selectedContact.emails.push('')
    },
    addAddress () {
      this.selectedContact.addresses.push('')
    },
    addPhoneNumber () {
      this.selectedContact.phone_numbers.push({phone_number: '', phone_type: ''})
    },
    editNewContact () {
      const newContact = {
        firstname: '',
        lastname: '',
        birthdate: null,
        addresses: [],
        emails: [''],
        phone_numbers: [{phone_number: '', phone_type: ''}]
      }
      this.$validator.reset()
      this.editingNewContact = true
      this.selectedContact = newContact
    },
    cancelEdit () {
      this.selectedContact = null
      this.editingNewContact = false
    },
    createContact () {
      this.$validator.validate()
        .then(valid => {
          if (valid) {
            backend.createContact(this.selectedContact)
              .then(({data}) => {
                this.contacts.push(data.contact)
                this.cancelEdit()
              })
              .catch(({response}) => {
                alert(response.data.errors)
              })
          }
        })
    },
    updateContact () {
      this.$validator.validate()
        .then(valid => {
          if (valid) {
            backend.updateContact(this.selectedContact)
              .then(() => {
                this.cancelEdit()
              })
              .catch(({response}) => {
                alert(response.data.errors)
              })
          }
        })
    },
    deleteContact () {
      backend.deleteContact(this.selectedContact)
        .then(() => {
          this.contacts = this.contacts.filter(c => {
            return c.id !== this.selectedContact.id
          })
          this.cancelEdit()
        })
    }
  },
  computed: {
    emailCount () {
      return this.selectedContact.emails.length
    },
    phoneNumberCount () {
      return this.selectedContact.phone_numbers.length
    },
    sortedContacts () {
      return this.contacts.slice(0).sort((c1, c2) => {
        return c1.firstname.localeCompare(c2.firstname)
      })
    }
  }
}
</script>
