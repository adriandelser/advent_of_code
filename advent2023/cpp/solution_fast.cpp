


#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
    std::ifstream file("input.txt");
    std::string line;
    std::vector<std::string> lines;

    if (file.is_open()) {
        while (getline(file, line)) {
            lines.push_back(line);
        }
        file.close();
    } else {
        std::cerr << "Unable to open file";
        return 1;
    }

    // Print the first line
    std::cout << lines[0] << std::endl;

    int sum = 0;
    for (const auto& l : lines) {
        std::string digits;
        for (char ch : l) {
            if (isdigit(ch)) {
                digits += ch;
            }
        }
        if (!digits.empty()) {
            int code = (digits.front() - '0') * 10 + (digits.back() - '0');
            sum += code;
        }
    }

    std::cout << sum << std::endl;

    return 0;
}
