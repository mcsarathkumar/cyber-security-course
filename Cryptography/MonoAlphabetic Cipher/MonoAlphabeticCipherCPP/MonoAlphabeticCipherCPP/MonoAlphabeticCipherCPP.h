// MonoAlphabeticCipherCPP.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <iterator>
#include <map>
#include <unordered_map>

constexpr short unsigned int ALPHABETS = 26;

using namespace std;

class MonoAlphabeticCipher {

private:

	void generateKeyValuePair(unordered_map<char, char> &keyValuePair, string &key, string operation) {
		transform(key.begin(), key.end(), key.begin(), ::tolower);
		unsigned short int lowerCaseFirstLetter = 97;
		unsigned short int upperCaseFirstLetter = 65;
		for each (char currentChar in key) {
			if (!operation.compare("encrypt")) {
				keyValuePair.insert({ char(lowerCaseFirstLetter++), currentChar });
				keyValuePair.insert({ char(upperCaseFirstLetter++), toupper(currentChar) });
			}
			else {
				keyValuePair.insert({ currentChar, char(lowerCaseFirstLetter++) });
				keyValuePair.insert({ toupper(currentChar), char(upperCaseFirstLetter++) });
			}
		}
	}

public:

	string encrypt(string plainText, string key) {
		if (key.length() != ALPHABETS) {
			return "Invalid Keys";
		}
		unordered_map<char, char> keyValPair;
		generateKeyValuePair(keyValPair, key, "encrypt");
		string cipherText = "";
		for each (char currentChar in plainText) {
			auto key = keyValPair.find(currentChar);
			if (key != keyValPair.end()) {
				cipherText += key->second;
			}
		}
		return cipherText;
	}

	string decrypt(string cipherText, string key) {
		if (key.length() != ALPHABETS) {
			return "Invalid Keys";
		}
		unordered_map<char, char> keyValPair;
		generateKeyValuePair(keyValPair, key, "decrypt");
		string plainText = "";
		for each (char currentChar in cipherText) {
			auto key = keyValPair.find(currentChar);
			if (key != keyValPair.end()) {
				plainText += key->second;
			}
		}
		return plainText;
	}

};