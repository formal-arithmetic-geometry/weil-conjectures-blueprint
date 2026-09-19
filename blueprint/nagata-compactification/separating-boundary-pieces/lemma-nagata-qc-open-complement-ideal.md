+++
id = "lemma-nagata-qc-open-complement-ideal"
kind = "lemma"
title = "Vanishing set of the open-complement ideal"
order = 383
lean = ["AlgebraicGeometry.Scheme.exists_finiteType_ideal_coe_support_eq_compl"]
uses = ["def-nagata-qc-open-complement-ideal", "lemma-nagata-qc-open-complement-ideal-exists"]
+++
The ideal $\mathcal I_Y(W)$ is finite type and quasi-coherent, and

$$
V(\mathcal I_Y(W))=Y\setminus W.
$$

## Proof

The witness supplied by
[lemma-nagata-qc-open-complement-ideal-exists] has exactly these
fields, and the definition selects its ideal component. Projecting those
fields proves the statement.
