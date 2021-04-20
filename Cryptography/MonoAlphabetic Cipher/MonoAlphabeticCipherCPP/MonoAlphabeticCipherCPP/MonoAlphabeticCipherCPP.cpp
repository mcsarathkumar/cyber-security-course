// MonoAlphabeticCipherCPP.cpp : Defines the entry point for the application.
//

#include "MonoAlphabeticCipherCPP.h"

int main()
{

	MonoAlphabeticCipher monoCipher;
	cout << monoCipher.encrypt("sarathkumar", "bcdefghijklmnopqrstuvwxyza") << endl;
	cout << monoCipher.decrypt("tbsbuilvnbs", "bcdefghijklmnopqrstuvwxyza");
	return 0;
}
