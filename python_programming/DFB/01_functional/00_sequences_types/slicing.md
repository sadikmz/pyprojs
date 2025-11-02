Slicing summary 

|      [i:j]       |    [i:j:k] k > 0     |     [i:j:k] k < 0     |
|:----------------:|:--------------------:|:---------------------:|
|   i > len(seq)   |       len(seq)       |     len(seq) - 1      |
|   j > len(seq)   |       len(seq)       |     len(seq) - 1      |
|      i < 0       | max(0, len(seq) + i) | max(-1, len(seq) + i) |
|      j < 0       | max(0, len(seq) + j) | max(-1, len(seq) + j) |
| i omitted / None |          0           |     len(seq) - 1      |
| j omitted / None |          0           |           1           |

