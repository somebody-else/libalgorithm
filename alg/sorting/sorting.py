from alg.common import ALG_DECORATOR


@ALG_DECORATOR
def insert_sorting(input: []):
    step = 0
    l = len(input)

    if l <= 1:
        return input

    print(l)
    for i in range(1, l):
        v = input[i]
        j = i
        while j > 0 and v > input[j-1]:
            step += 1
            # print("{} > {}".format(v, input[j-1]))
            input[j] = input[j-1]
            # print(input)
            j -= 1

        input[j] = v
        # print(input)

    print("toal steps: {}".format(step))
    return input


@ALG_DECORATOR
def select_sorting(input: []):
    step = 0
    output = []
    l = len(input)
    for i in range(0, l):
        v = input[i]
        idx = i
        for j in range(i, l):
            step += 1
            if input[j] >= input[i]:
                input[i] = input[j]
                idx = j

        input[idx] = v
        # input.remove(v)
    print("total {} steps".format(step))
    return input


@ALG_DECORATOR
def merge_sorting(input: []):

    def merge(in1, in2):
        output = []
        l1 = len(in1)
        l2 = len(in2)
        l = l1+ l2
        idx1 = idx2 = 0
        for i in range(l):

            if in1[idx1] > in2[idx2]:
                output.append(in1[idx1])
                idx1 += 1
            else:
                output.append(in2[idx2])
                idx2 += 1

            if idx1 >= l1:
                output = output + in2[idx2:]
                break
            if idx2 >= l2:
                output = output + in1[idx1:]
                break
        return output


    l = len(input)
    half = int(l/2)
    if l > 1:
        output = merge(merge_sorting(list(input[: half])), merge_sorting(list(input[half:])))
    else:
        return input
    return output

@ALG_DECORATOR
def python_sorting(input: []):
     input.sort(reverse=1)
     return input


if __name__ == '__main__':
    input = list(range(10001))

    #output = insert_sorting(input)

    #output = python_sorting(input)

    # output = select_sorting(input)

    output = merge_sorting(input)
    print(output)



