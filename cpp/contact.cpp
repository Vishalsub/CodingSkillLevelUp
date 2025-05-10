// 🎯 Goals:
// Practice classes, methods, constructors
// Use std::vector, std::unique_ptr
// Validate user inputs (name, phone, email)
// Practice file save/load with I/O streams
// Reinforce use of const, &, pointers
// Add a basic menu system in terminal

#include <iostream>
#include <string>
#include <cctype>
#include <regex>
#include <vector>

struct Contacts{
    std::string name;
    std::string email;
    std::string phone;

    void display() const{
        std::cout << "-------Userinfo-------" << "\n";
        std::cout << "Name :" << name << "\n";
        std::cout << "Email :" << email << "\n";
        std::cout << "phone :" << phone << "\n";     
    }
    bool isValid() const{
        if(!name.empty()) return false;
        for(char a : name){
            if(!std::isalpha(a) && a!=' ') return false;
        }
        std::regex pattern(R"(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b)");
        std::regex pattern(R"(/+/d{1,3}/d{7,12})");
        return std::regex_match(email, pattern),std::regex_match(phone, pattern);

    }
};

class contactBooking{
private:
    std::vector<Contacts> contacts;
public:
    void addContact(const Contacts& contact){
        if(contact.isValid()){
            contacts.push_back(contact);
        }
        else{
            std::cerr << "Invalid";
        }
    }
    void searchByName(const std::string& query) const{
        bool search = false;
        for(const auto& c : contacts){
            if(c.name.find(query)!= std::string::npos);
            bool search = true;
        }
        if(!search) std::cout << "couldn't find it";
    }
    void saveToFile(const std::string& filename) const{

    }
    void loadToFile(const std::string& filename){

    }
    void deleteByFile(const std::string& name){

    }
    void showAll() const{
        if(contacts.empty()){
            std::cout << "empty just like me";
            return;
        }
        else {
            for(const auto& c : contacts){
                c.display();

            }
        }

    }
};


int main(){

}