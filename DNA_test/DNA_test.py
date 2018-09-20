from scipy import stats



def get_ages():
    ages = [] 
    f = open("age.txt", 'r', encoding="utf-8")
    ages = f.read().split()
    for i in range(len(ages)): 
       ages[i] = int(ages[i]) 
    f.close()
    return ages 




def get_gene_data(file):
    gene_data = file.readline().split(" ")
    gene_name = gene_data.pop(0)

    for i in range(len(gene_data)):
        gene_data[i] = float(gene_data[i])
    return gene_name, gene_data



def calculate_spearman_corr(file):
    gene_names = []
    rvalues = []
    arr1 = get_ages()   
    d = {}
    while True:
        name, arr2 = get_gene_data(file)
        if len(arr2) == 0 :
            break
        rvalue, tmp = stats.spearmanr(arr1, arr2)
        rvalues.append(rvalue)
        gene_names.append(name)

    for j in range(len(rvalues)):
        d[gene_names[j]] = rvalues[j]
    d = sorted(d.items(), key=lambda item: (-item[1])) 

    for i in range(10):
        print(str(i + 1) + ")" + str(d[i]))


def main():
    file = open("gene_data.txt", 'r', encoding="utf-8")
    print("Spearman's correlation.\nThe first 10 genes that have the highest correlation coefficient are:")
    calculate_spearman_corr(file)
    file.close()
    
main()

