// CaesarCipherCPP.cpp : Defines the entry point for the application.
//

#include "CaesarCipherCPP.h"

int main()
{
	CaesarCipher cc;
	string plain = "SARATHKUMAR";
	string cipher = cc.encrypt(plain, 10);
	cout << cipher << endl;
	cout << cc.decrypt(cipher, 10) << endl;
	return 0;
}