<template>
  <div class="max-w-lg mx-auto rounded overflow-hidden shadow-lg">
    <div class="flex">

      <ul class="contact-list">
        <li v-for="contact in sortedContacts" :key="contact.id">
          <a @click="selectedContact = contact"> {{ contact.firstname }} {{ contact.lastname }} </a>
        </li>
      </ul>

      <div class="contact-editor" v-if="selectedContact">
        <input class="contact-editor__input" v-model="selectedContact.firstname" />
        <input class="contact-editor__input" v-model="selectedContact.lastname" />
        <datepicker input-class="contact-editor__input" v-model="selectedContact.birthdate"></datepicker>

        <div>
          <h4>Emails</h4>
          <div v-for="(email, index) in selectedContact.emails" :key="`email-${index}`">
            <input class="contact-editor__input" v-model="selectedContact.emails[index]" />
            <button class="contact-editor__btn contact-editor__btn--delete" v-if="emailCount > 1" @click="selectedContact.emails.splice(index, 1)">delete</button>
          </div>
          <button class="contact-editor__btn contact-editor__btn--add-data" @click="addEmail">Add Email</button>
        </div>

        <div>
          <h4>Addresses</h4>
          <div v-for="(address, index) in selectedContact.addresses" :key="`address-${index}`">
            <input class="contact-editor__input" v-model="selectedContact.addresses[index]" />
            <button class="contact-editor__btn contact-editor__btn--delete" @click="selectedContact.addresses.splice(index, 1)">delete</button>
          </div>
          <button class="contact-editor__btn contact-editor__btn--add-data" @click="addAddress">Add address</button>
        </div>

        <div>
          <h4>Phone numbers</h4>
          <div v-for="(phoneNumber, index) in selectedContact.phoneNumbers" :key="`phone-number-${index}`">
            <input class="contact-editor__input" v-model="selectedContact.phoneNumbers[index].number" />
            <select v-model="selectedContact.phoneNumbers[index].type">
              <option>Personal</option>
              <option>Work</option>
              <option>Home</option>
            </select>
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
  import Datepicker from 'vuejs-datepicker';

  export default {
    components: {
      Datepicker
    },
    data() {
      return {
        selectedContact: null,
        contacts: [
          { id: 1, 
            firstname: "Robinson",
            lastname: "Rodriguez",
            birthdate: null,
            emails: [""],
            addresses: [],
            phoneNumbers: [
              { number: "123456", type: "Home" },
              { number: "12131", type: "Work" }
            ] 
          }
        ]
      }
    },
    methods: {
      addEmail() {
        this.selectedContact.emails.push("")
      },
      addAddress() {
        this.selectedContact.addresses.push("")
      },
      addPhoneNumber() {
        this.selectedContact.phoneNumbers.push({number: "", type: ""})
      },
      onChange(event) {
        console.log(event)
      },
      syncContact() {
      }
    },
    computed: {
      emailCount () {
        return this.selectedContact.emails.length
      },
      sortedContacts () {
        return this.contacts.sort((c1, c2) => {
          return c1.firstname.localeCompare(c2.firstname)
        })
      }
    }
  }
</script>
