# Pet Relation Extraction Dataset
- Naver Boostcamp AI Tech 3
- NLP Data Annotation Project

## [Solution Presentation](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-08/blob/main/assets/08_presentation.pdf)

## [Wrapup Report](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-08/blob/main/assets/Data_Annotation_NLP_%ED%8C%80_%EB%A6%AC%ED%8F%AC%ED%8A%B8(8%EC%A1%B0).pdf)

## [Guideline](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-08/blob/main/assets/08_guideline.pdf)

## [Relation Map](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-08/blob/main/assets/08_relation.xlsx)

## Members

임동진_T3180|정재윤_T3201|조설아_T3205|허치영_T3238|이보림_T3246|
:-:|:-:|:-:|:-:|:-:|
[Github](https://github.com/idj7183)|[Github](https://github.com/kma7574)|[Github](https://github.com/jarammm)|[Github](https://github.com/mooncy0421)|[Github](https://github.com/bo-lim)|

## Data Overview
- Train data : 1579
- Test data : 176
- Number of class : 10
    ```
    '동물:서식지' '동물:대체표현' '동물:신체적특징' '동물:비신체적특징' '동물:사냥감' '동물:역할' '동물:유래' '동물:개체수' 
    '집단:하위집단' '관계 없음' 
    ```

## Results (KLUE/BERT-base)
- **Fleiss' Kappa** : 0.79
- **Micro F1** : 57.2581
- **AUPRC** : 60.4493
-  Selected as **Novel King**
