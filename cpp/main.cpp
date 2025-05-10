#include <iostream>
#include <string>
#include <cctype>
#include <regex>
#include <memory>

class UserDetails{
public:
    std::string name;
    int Age;
    std::string email;
    std::string phone;

    void display() const{
        std::cout << "-------Userinfo-------" << "\n";
        std::cout << "Name : " << name <<  "\n";
        std::cout << "agee : " << Age << "\n";
        std::cout << "mail : " << email << "\n";
        std::cout << "phone number : " << phone << "\n";
    }
};

void getInput(const std::string& label, std::string& input){
    std::cout << "Enter" << label << ":";
    std::getline(std::cin, input);  // look into
}

bool isValidname(const std::string& name){
    if(name.empty()) return false;
    for(char a: name){
        if(!std::isalpha(a) && a != ' ') return false;
    }
    return true;
}

bool isvalidage(const std::string& agestr, int& ageout){
    if(agestr.empty()) return false;
    for (char a: agestr){
        if(!std::isdigit(a)) return false;
    }
    ageout = std::stoi(agestr);
    return ageout >= 0 && ageout <= 120;
}

bool isValidemail(const std::string& email){
    std::regex pattern(R"(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b)");
    return std::regex_match(email, pattern);
}

bool isValidphone(const std::string& phone){
    // std::regex pattern(R"(\+\d{1,3}\d{7,12})");
    // return std::regex_match(phone, pattern);
    std::regex pattern(R"(\+\d{1,3}\d{7,12})"); // e.g., +65xxxxxxxxx
    return std::regex_match(phone, pattern);
}

int main(){
    // UserDetails* user = new UserDetails(); 
    std::unique_ptr<UserDetails> user = std::make_unique<UserDetails>();
    std::string agestr;
    bool valid = true;

    getInput("your full name", user->name);
    if(!isValidname(user->name)){
        std::cerr << " Invalid name. Letters and spaces only.\n";
        valid = false;
    }
    getInput("your age", agestr);
    if(!isvalidage(agestr, user->Age)){
        std::cerr << " Invalid age..\n";
        valid = false;
    }

    getInput("Your email", user->email);
    if(!isValidemail(user->email)){
        std::cerr << " Invalid email..\n";
        valid = false;
    }

    getInput("Your Phone Nuber", user->phone);
    if(!isValidphone(user->phone)){
        std::cerr << " Invalid phone number..\n";
        valid = false;
    }

    if(valid){
        user->display();
    }
    else {
        std::cerr << "⚠️ Burnout — input validation failed.\n";
    }
    // delete user; // Delete the pointer 
    return 0;
}