// CaesarCipherCPP.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#include <iostream>
#include <string.h>

constexpr short unsigned int LOWER_CASE_A = 97;
constexpr short unsigned int LOWER_CASE_Z = 122;
constexpr short unsigned int UPPER_CASE_A = 65;
constexpr short unsigned int UPPER_CASE_Z = 90;
constexpr short unsigned int ALPHABETS_COUNT = 26;

using namespace std;

class CaesarCipher {

public:

    string encrypt(string plainText, int shift) {
        bool validInput = true;
        string cipherText = "";
        for (unsigned short int i = 0; i < plainText.length(); i++) {
            int charAscii = (int)plainText[i];
            if (charAscii >= LOWER_CASE_A && charAscii <= LOWER_CASE_Z) {
                int valueAfterShift = charAscii - LOWER_CASE_A + shift;
                if (valueAfterShift >= ALPHABETS_COUNT) {
                    valueAfterShift -= ALPHABETS_COUNT;
                }
                cipherText += char(valueAfterShift + LOWER_CASE_A);
            }
            else if (charAscii >= UPPER_CASE_A && charAscii <= UPPER_CASE_Z) {
                int valueAfterShift = charAscii - UPPER_CASE_A + shift;
                if (valueAfterShift >= ALPHABETS_COUNT) {
                    valueAfterShift -= ALPHABETS_COUNT;
                }
                cipherText += char(valueAfterShift + UPPER_CASE_A);
            }
            else {
                validInput = false;
                break;
            }
        }
        return !validInput ? "Invalid Input" : cipherText;
    }

    string decrypt(string cipherText, int shift) {
        bool validInput = true;
        string plainText = "";
        for (unsigned short int i = 0; i < cipherText.length(); i++) {
            int charAscii = (int)cipherText[i];
            if (charAscii >= LOWER_CASE_A && charAscii <= LOWER_CASE_Z) {
                int valueBeforeShift = charAscii - LOWER_CASE_A - shift;
                if (valueBeforeShift < 0) {
                    valueBeforeShift += ALPHABETS_COUNT;
                }
                plainText += char(valueBeforeShift + LOWER_CASE_A);
            }
            else if (charAscii >= UPPER_CASE_A && charAscii <= UPPER_CASE_Z) {
                int valueBeforeShift = charAscii - UPPER_CASE_A - shift;
                if (valueBeforeShift < 0) {
                    valueBeforeShift += ALPHABETS_COUNT;
                }
                plainText += char(valueBeforeShift + UPPER_CASE_A);
            }
            else {
                validInput = false;
                break;
            }
        }
        return !validInput ? "Invalid Input" : plainText.c_str();
    }

};