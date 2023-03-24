arr = ["flower"]
str= ["flower","flow","flight"]
def longest_prefix(arr):
    # The longest common prefix of an empty array is "".
    final=""
    if len(arr)==0:
      print("Longest common prefix:",final)
    # The longest common prefix of an array containing
    # only one element is that element itself.
    elif len(arr) == 1:
      print("Longest common prefix:", arr[0])
    else:
      # Sort the array
      arr.sort()
      result = ""
      # Compare the first and the last string character
      # by character.
      for i in range(len(arr[0])):
          #  If the characters match, append the character to
          #  the result.
          if arr[0][i] == arr[-1][i]:
              result += arr[0][i]
          # Else, stop the comparison
          else:
              break
      return result

longest_prefix(arr)