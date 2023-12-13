def nums_que_comencen_per_a(llista_noms):
    noms_comencen_per_a = [nom for nom in llista_noms if nom.lower().startswith('a')]
    return len(noms_comencen_per_a)

def main():
    llista_noms = input("Introdueix noms separats per espais: ").split()
    quantitat_noms = nums_que_comencen_per_a(llista_noms)
    print(f"Hi ha {quantitat_noms} noms que comencen per la lletra 'a'.")

if __name__ == "__main__":
    main()