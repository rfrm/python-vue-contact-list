<template>
  <div>
    <div v-for="contact in sortedContacts" :key="contact.id">
      <a @click="selectedContact = contact"> {{ contact.firstname }} {{ contact.lastname }} </a>
    </div>
    <div v-if="selectedContact">
      <input v-model="selectedContact.firstname" />
      <input v-model="selectedContact.lastname" />
      <datepicker v-model="selectedContact.birthdate"></datepicker>
      <div v-for="(email, index) in selectedContact.emails" :key="`email-${index}`">
        <input v-model="selectedContact.emails[index]" />
        <a v-if="emailCount > 1" @click="selectedContact.emails.splice(index, 1)">delete</a>
      </div>
      <button @click="addEmail">Add Email</button>
      <div v-for="(address, index) in selectedContact.addresses" :key="`address-${index}`">
        <input v-model="selectedContact.addresses[index]" />
        <a @click="selectedContact.addresses.splice(index, 1)">delete</a>
      </div>
      <button @click="addAddress">Add address</button>
      <div v-for="(phoneNumber, index) in selectedContact.phoneNumbers" :key="`phone-number-${index}`">
        <input v-model="selectedContact.phoneNumbers[index].number" />
        <select v-model="selectedContact.phoneNumbers[index].type">
          <option>Personal</option>
          <option>Work</option>
          <option>Home</option>
        </select>
        <a @click="selectedContact.phoneNumbers.splice(index, 1)">delete</a>
      </div>
      <button @click="addPhoneNumber">Add phone</button>
      <hr>
      <button @click="syncContact">Save</button>
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
          },
          { id: 2, firstname: "Naveed", lastname: "Ahmed", birthdate: null, emails: [""], addresses: [], phoneNumbers: [] }
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
