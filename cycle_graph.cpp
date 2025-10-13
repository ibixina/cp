#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int n;
vector<vector<int>> adj;
vector<char> color; // visited or not
vector<int> parent;
int cycle_start, cycle_end;


bool dfs(int v){
  color[v] = 1; // mark the vertex as visited
  
  for (int u: adj[v]){
    if (color[u] == 0){
      parent[u] = v;
      if (dfs(u)) return true;
    } 
    else if (color[u] == 1) {
      cycle_end = v;
      cycle_start = u;
      return true;
    }
  }

  color[v] = 2; // mark the vertex as visited

  return false;
}

void find_cycle(){
  color.assign(n, 0); // assign 0 to all vertices
  parent.assign(n, -1); // assign -1 to all vertices
  cycle_start = -1;

  for (int v = 0; v < n; v++) { // visit all vertices
    if (color[v] == 0 && dfs(v)) break; // if there is a cycle, break the loop
  }

  if (cycle_start == -1) { // if there is no cycle
    cout << " Acyclic" << endl;
  } else {
    vector<int> cycle;

    cycle.push_back(cycle_start); // start exploring the cycle from the first vertex
    for (int v = cycle_end; v != cycle_start; v = parent[v]) cycle.push_back(v);
    cycle.push_back(cycle_start);
    reverse(cycle.begin(), cycle.end()); // reverse the cycle to get it from start to end

    cout << " Cycle: ";
    for (int v : cycle) cout << v << " ";
    cout << endl;

  }
}
