+++
kind  = "proof"
of    = "sk-thm-fe"
+++
Substitute $q^{-d}T^{-1}$ into the factorization
$Z=\prod_iP_{i,\ell}^{(-1)^{i+1}}$ of [sk-thm-tracetodeterminant] and
replace each factor by [sk-prop-reciprocity]; reindexing $i\mapsto2d-i$
turns the product into $\prod_iP_{i,\ell}^{(-1)^{i+1}}$ again, times the
constant $\prod_i\bigl((-1)^{b_i}D_i^{-1}\bigr)^{(-1)^{i+1}}$ and the monomial
$T^{\sum_i(-1)^{i+1}(-b_i)}=T^{\sum_i(-1)^{i}b_i}=T^{\chi}$. The constant is
$\prod_iD_i^{(-1)^{i}}$ up to the sign $(-1)^{\sum_i(-1)^{i+1}b_i} =(-1)^{-\chi}=(-1)^{\chi}$. By [sk-prop-reciprocity] $d\chi$ is even, so
$q^{d\chi/2}$ is defined and the constant is
$\varepsilon q^{d\chi/2}$; this is the displayed identity.
