# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
#  *   en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización
#  *   y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#  *   y a continuación los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no númericos y con más
#  *   de 11 dígitos (o el número de dígitos que quieras).
#  * - También se debe proponer una operación de finalización del programa.
#  */

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                break

    def update_contact(self, name, new_phone_number):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                break

    def sort_contacts(self):
        self.contacts.sort(key=lambda x: x.name)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

# Test the ContactBook class
if __name__ == "__main__":
    contact_book = ContactBook()

    # Add contacts
    contact_book.add_contact(Contact("John", "123456789"))
    contact_book.add_contact(Contact("Alice", "987654321"))

    # Sort contacts
    contact_book.sort_contacts()

    # Search contact
    contact = contact_book.search_contact("Alice")
    if contact:
        print("Found contact:", contact.name, contact.phone_number)
    else:
        print("Contact not found")

    # Update contact
    contact_book.update_contact("Alice", "555555555")

    # Delete contact
    contact_book.delete_contact("John")







