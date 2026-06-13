#Inventio interface
 
import streamlit as st

st.title("Inventio")
st.text("Ajout d'un nouvel objet.")
item_type =st.selectbox("Type d'objet *", ["Livre", "Puzzle", "Vêtement", "Autre"],index=None,placeholder="Sélectionnez le type d'objet ici.")
item_name = st.text_input("Nom de l'objet *", placeholder="Entrez le nom de l'objet ici.")
item_used = st.checkbox('Déjà utilisé')
#A améliorer : terminologie "créateur" à revoir car pas forcément un créateur pour tous les types d'objets (ex : vêtement, puzzle, etc), ni clair pour un livre
item_author = st.text_input("Auteur ou marque", placeholder="Entrez le nom de l'auteur ou de la marque ici.")
#A améliorer : catégorie que l'utilisateur aura préparamétré pour chaque type d'objet (livre : roman, BD, manga, etc ; vêtement : haut, bas, chaussures, etc)
item_category = st.text_input("Catégorie", placeholder="Entrez la catégorie de l'objet ici.")
#A améliorer : définir l'alerte coût pour les autres types d'objets.
item_cost = st.number_input("Coût à l'achat", value=None,format="%.2f", min_value=0.0, step=0.01)
#A faire : afficher € sur la même ligne que le champ de saisie du coût à l'achat, lorsque sera fait la disposition en colonne
st.text("€")
if item_cost == 0:
    st.warning("Vous avez indiqué 0 €, confirmez-vous que l'objet vous a été offert ?")
if item_type == "Livre" and item_cost is not None and item_cost > 100:
    st.warning("Le coût à l'achat indiqué semble très élevé pour un objet de ce type. S'agit-il d'une édition rare ou d'une erreur de saisie ?")
st.caption("Indiquez 0 € si l'objet vous a été offert.")
item_decision = st.selectbox("Décision", ["Garder", "Vendre", "Donner", "Jeter","En sursis"],index=None,placeholder="Indiquez votre décision ici.")
item_comment = st.text_input("Commentaire", placeholder="Si vous souhaitez ajouter un commentaire sur votre décision, indiquez-le ici.")
#A améliorer : lieu de stockage que l'utilisateur aura préparamétré
item_storage_location = st.text_input("Lieu de stockage", placeholder="Entrez le lieu où est rangé l'objet ici.")
st.text("*Champs obligatoires")

#Check input values

error = False
text_error=""

if st.button("Ajouter l'objet à ma maison"):
    if item_type is None:
        error=True
        text_error="- Sélectionnez un type d'objet. \n "
    if item_name == "":
        error=True
        text_error=text_error+"- Indiquez le nom de l'objet. \n "
    if item_cost is None :
        error=True
        text_error=text_error+"- Indiquez le coût à l'achat de l'objet. S'il vous a été offert, indiquez 0 €."
    if error:
        st.error(text_error)
    else:
        #Data storage
        new_item = {
            "type": item_type,
            "name": item_name,
            "used": item_used,
            "author": item_author,
            "category": item_category,
            "cost": item_cost,
            "decision": item_decision,
            "comment": item_comment,
            "storage_location": item_storage_location
        }
        st.success("Ce " + str(new_item["type"]).lower() + " " + str(new_item["name"]) + " a été ajouté à votre maison avec succès.")