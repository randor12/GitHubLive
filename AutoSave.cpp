/*
 * Ryan Nicholas
 * Make an auto save function
 */

#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
#include <vector>

using namespace std;
namespace fs = std::filesystem;

/**
 * This is the main class
 * @return		returns 0
 */
int main()
{
	string path;
	vector<string> files;
	cout << "Input the path: " << endl;
	cin >> path;

	for (const auto& entry : fs::directory_iterator(path))
	{
		files.push_back(entry.path());
	}

	for (string getFile : files) {
		if (!getFile._Equal(".git")) {
			ofstream outfile;
			outfile.open(getFile, ios_base::app);
			outfile.close();
		}
	}

	return 0;
}