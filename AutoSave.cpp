/*
 * Ryan Nicholas
 * Make an auto save function
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <filesystem>
#include <Windows.h>
#include <tchar.h>
#include <stdio.h>
#include <corecrt_wstring.h>

using namespace std;
namespace fs = std::experimental::filesystem;

/**
 * Following code was found on stack overflow
 */
vector<wstring> get_all_files_names_within_folder(wstring folder)
{
	vector<wstring> names = {};
	wstring search_path = folder;
	WIN32_FIND_DATA fd;
	HANDLE hFind = ::FindFirstFile(search_path.c_str(), &fd);
	if (hFind != INVALID_HANDLE_VALUE) {
		do {
			// read all (real) files in current folder
			// , delete '!' read other 2 default folder . and ..
			if (!(fd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
				names.push_back(fd.cFileName);
			}
		} while (::FindNextFile(hFind, &fd));
		::FindClose(hFind);
	}
	return names;
}

/**
 * Convert a string into a wstring
 */
wstring toWstring(string word)
{
	wstring temp(word.begin(), word.end());

	return temp;
}

/**
 * converts a wstring to a string
 */
string toString(wstring word)
{
	string temp(word.begin(), word.end());

	return temp;
}

/**
 * This is the main class
 * @return		returns 0
 */
int main()
{
	string path;
	//vector<int> files = {};
	cout << "Input the path: " << endl;
	cin >> path;

	wstring folder = toWstring(path);

	vector<wstring> files = get_all_files_names_within_folder(folder);

	for (wstring getFile : files) {
		string actualFile = toString(getFile);
		cout << actualFile << endl;
	}

	/*
	for (string getFile : files) {
		if (!getFile._Equal(".git")) {
			ofstream outfile;
			outfile.open(getFile, ios_base::app);
			outfile.close();
		}
	}
	*/

	return 0;
}