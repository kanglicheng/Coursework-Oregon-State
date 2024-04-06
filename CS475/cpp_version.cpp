#include <iostream>

int main() {
    if (__cplusplus == 199711L) {
        std::cout << "Compiled with C++98\n";
    } else if (__cplusplus == 201103L) {
        std::cout << "Compiled with C++11\n";
    } else if (__cplusplus == 201402L) {
        std::cout << "Compiled with C++14\n";
    } else if (__cplusplus == 201703L) {
        std::cout << "Compiled with C++17\n";
    } else if (__cplusplus == 202002L) {
        std::cout << "Compiled with C++20\n";
    } else {
        std::cout << "Compiled with a version earlier than C++98 or a non-standard compiler\n";
    }

    return 0;
}