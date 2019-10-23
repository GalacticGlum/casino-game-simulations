/**
 * Simulates the probabilities.
 */

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <random>
#include <iterator>

typedef unsigned long long ull;
#define TRIALS 100000000
#define MAX_SUM 44
const std::vector<int> board = {
    4, 3, 2, 4, 1, 4, 2, 3, 4,
    3, 4, 5, 3, 6, 3, 5, 4, 3,
    4, 3, 2, 4, 1, 4, 2, 3, 4,
    3, 4, 5, 3, 6, 3, 5, 4, 3,
    4, 3, 2, 4, 1, 4, 2, 3, 4,
    3, 4, 5, 3, 6, 3, 5, 4, 3,
    4, 3, 2, 4, 1, 4, 2, 3, 4,
    3, 4, 5, 3, 6, 3, 5, 4, 3,
    4, 3, 2, 4, 1, 4, 2, 3, 4  
};

ull event_outcomes[MAX_SUM + 1];

int main()
{
    std::fill(std::begin(event_outcomes), std::end(event_outcomes), 0);

    std::mt19937 random = std::mt19937{std::random_device{}()};
    for (ull i = 0; i < TRIALS; ++i)
    {
        std::vector<int> selection;
        std::sample(board.begin(), board.end(), std::back_inserter(selection), 8, random);

        int sum = 0;
        for (auto& v : selection)
        {
            sum += v;
        }

        event_outcomes[sum] += 1;
    }

    std::unordered_map<int, double> probability_distribution;
    for (int i = 0; i < MAX_SUM; ++i)
    {
        probability_distribution[i] = event_outcomes[i] / (double)TRIALS * 100.0;
    }

    std::vector<std::pair<int, double>> probabilities(probability_distribution.begin(), probability_distribution.end());
    std::sort(probabilities.begin(), probabilities.end());
    for (auto& key : probabilities)
    {
        std::cout << key.first << ": " << key.second << "\n";
    }
}