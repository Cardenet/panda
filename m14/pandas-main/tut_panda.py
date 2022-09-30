import numpy as np
import pandas as pd
 
# create a serie

s = pd.Series([1,3,5,np.nan,6,8])
print(s)
animal_list=["Spider","Cocodrile","Panda","Rex"]
legs_list=[8,4,4,2]
serie_animales=pd.Series(data=legs_list, dtype=str, index=animal_list)
print(serie_animales)
# create a dataframe

dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
# Test dataframes
# Podem convertir un diccionari que els seus valors siguin llistes en un Dataframe.
dict_animals = {'num_legs': [2, 4, 0, 8], 'num_wings': [2, 0, 0, 0]}
# Com en les sèries, el valor dels índex el podem passar com una llista.
name_animals = ['falcon', 'dog', 'snail', 'spider']
df_animals = pd.DataFrame(data=dict_animals, index=name_animals)
print(df_animals)

# create a dataframe with a dictionary

df2 = pd.DataFrame(

    {

        "A": 1.0,

        "B": pd.Timestamp("20130102"),

        "C": pd.Series(1, index=list(range(4)), dtype="float32"),

        "D": np.array([3] * 4, dtype="int32"),

        "E": pd.Categorical(["test", "train", "test", "train"]),

        "F": "foo",

    }

)
print(df2)



animals_df = pd.Series(data=['falcon', 'dog', 'snail', 'spider'], dtype="string")
df3 = pd.DataFrame(
    {
        "A": [1.0] + [np.nan] * 2 + [3.0],
        "B": pd.date_range("20220101", periods=4, freq='D'),
        "C": animals_df,
        "D": pd.Categorical(["Male", "Female", "NS/NC", "Female"]),
        "E": "foo",
    }
)
print(df3)

#les notes de dawbio amb dataframe
student_list=["John","Mary","Lucy","Peter","Alex","William","Pepe"]
grades_list = [7,9,8,4,5,5,10]
wants_dual_list = [False,True,False,True,True,False,False]
student_comment=["kek1","kek2","kek3","kek4","kek5","kek6","kek7"]
datos: dict[list] = {"grade": grades_list,
      "dual": wants_dual_list,"comment":student_comment}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
print(students_frame)
#les notes de dawbio amb dataframe
student_list=["John","Mary","Lucy","Peter","Ann","Tom"]
grades_list = [7,9,8,4,10,6]
wants_dual_list = [False,True,False,True,True,True]
wants_dualipa_list = [True]
start_date = pd.date_range("20210101", periods=6)

datos: dict[list] = {"grade": grades_list,
      "dual": wants_dual_list, "student_list" : student_list}

students_frame = pd.DataFrame(
    index=student_list,
    data=datos
)
#print(students_frame)

# Ordenar numèric
students_frame_sorted = students_frame.sort_values(by=["grade"],axis=0,ascending=False)
print(students_frame_sorted)

# Ordenar alfabètic.
students_frame_sorted = students_frame.sort_values(by=["student_list"],ascending=True)
print(students_frame_sorted)
# Utilitzar sempre localització d'un atribut
# .loc rep 2 parametres('enfonsar-se','bucejar')
print("Lucy grade = ",students_frame.loc["Lucy","grade"])


#si vull totes les notes dels estudiants, a la fila poso un slice buit
students_frame.loc[:,"grade"]

#La primera coordenada capbusada | i despres bucejo -> però amb numèrics.
students_frame.iloc[0,1]


# Les 2 consultes retornen el mateix resultat.
# at = loc opt.
print(students_frame.at["Lucy","grade"])
# iat = loc opt.
print(students_frame.iat[2,0])

#Podemos devolver una lista de varias filas, devuelve una lista
students_frame.loc[["Mary","Lucy"],"grade"]

#Podem retornar una llista de varies files, i retorna una llista
students_frame.loc[["Mary","Lucy"],
                   ["grade","dual"]]