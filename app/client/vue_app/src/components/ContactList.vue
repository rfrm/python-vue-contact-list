<template>
  <div class="max-w-lg mx-auto rounded overflow-hidden shadow-lg">
    <div class="flex">

      <ul class="contact-list">
        <li v-for="contact in sortedContacts" :key="contact.id">
          <a @click="selectedContact = contact"> {{ contact.firstname }} {{ contact.lastname }} </a>
        </li>
      </ul>

      <div class="contact-editor" v-if="selectedContact">
        <div class="contact-editor__data-section">
          <input class="contact-editor__input" placeholder="First name" v-model="selectedContact.firstname" />
          <input class="contact-editor__input" placeholder="Last name"  v-model="selectedContact.lastname" />
          <datepicker input-class="contact-editor__input" placeholder="birthdate" v-model="selectedContact.birthdate"></datepicker>
        </div>

        <div class="contact-editor__data-section">
          <h4>Emails</h4>
          <div class="mb-1" v-for="(email, index) in selectedContact.emails" :key="`email-${index}`">
            <input class="contact-editor__input" :placeholder="`Email ${index+1}`" v-model="selectedContact.emails[index]" />
            <button class="contact-editor__btn contact-editor__btn--delete" v-if="emailCount > 1" @click="selectedContact.emails.splice(index, 1)">delete</button>
          </div>
          <button class="contact-editor__btn contact-editor__btn--add-data" @click="addEmail">Add Email</button>
        </div>

        <div class="contact-editor__data-section">
          <h4>Addresses</h4>
          <div class="mb-1" v-for="(address, index) in selectedContact.addresses" :key="`address-${index}`">
            <input class="contact-editor__input" :placeholder="`Address ${index+1}`" v-model="selectedContact.addresses[index]" />
            <button class="contact-editor__btn contact-editor__btn--delete" @click="selectedContact.addresses.splice(index, 1)">delete</button>
          </div>
          <button class="contact-editor__btn contact-editor__btn--add-data" @click="addAddress">Add address</button>
        </div>

        <div class="contact-editor__data-section">
          <h4>Phone numbers</h4>
          <div class="flex mb-1" v-for="(phoneNumber, index) in selectedContact.phoneNumbers" :key="`phone-number-${index}`">
            <input class="contact-editor__input w-1/3 mr-1" :placeholder="`Phone number ${index+1}`" v-model="selectedContact.phoneNumbers[index].number" />
            <div class="relative w-1/3 mr-1">
              <select class="contact-editor__phone-number__type-select" v-model="selectedContact.phoneNumbers[index].type">
                <option>Personal</option>
                <option>Work</option>
                <option>Home</option>
              </select>
              <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
              </div>
            </div>
            <button class="contact-editor__btn contact-editor__btn--delete" @click="selectedContact.phoneNumbers.splice(index, 1)">delete</button>
          </div>
          <button class="contact-editor__btn contact-editor__btn--add-data" @click="addPhoneNumber">Add phone</button>
        </div>
        <hr>
        <button class="contact-editor__btn" @click="syncContact">Save</button>
      </div>
    </div>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker'

export default {
  components: {
    Datepicker
  },
  data () {
    return {
      selectedContact: null,
      contacts: [
        { id: 1,
          firstname: 'Robinson',
          lastname: 'Rodriguez',
          birthdate: null,
          emails: [''],
          addresses: [],
          phoneNumbers: [
            { number: '123456', type: 'Home' },
            { number: '12131', type: 'Work' }
          ]
        }
      ]
    }
  },
  methods: {
    addEmail () {
      this.selectedContact.emails.push('')
    },
    addAddress () {
      this.selectedContact.addresses.push('')
    },
    addPhoneNumber () {
      this.selectedContact.phoneNumbers.push({number: '', type: ''})
    }
  },
  computed: {
    emailCount () {
      return this.selectedContact.emails.length
    },
    sortedContacts () {
      return this.contacts.slice(0).sort((c1, c2) => {
        return c1.firstname.localeCompare(c2.firstname)
      })
    }
  }
}
</script>
