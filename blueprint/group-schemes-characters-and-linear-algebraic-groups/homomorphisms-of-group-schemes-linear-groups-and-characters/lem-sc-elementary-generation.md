+++
id = "lem-sc-elementary-generation"
kind = "lemma"
title = "Gaussian elimination"
order = 3915
lean = ["Matrix.GeneralLinearGroup.exists_elementary_diagonal_factorization"]
uses = ["def-sc-general-linear-group"]
+++
Let $k$ be a field and $c\geq1$. For $i\neq j$ and $a\in k$ let
$E_{ij}(a)=1+aE_{ij}\in\mathrm{GL}_c(k)$ be the corresponding elementary
matrix [def-sc-general-linear-group]. Then every $g\in\mathrm{GL}_c(k)$ is
a product of elementary matrices and one diagonal matrix.

## Proof

We prove the stronger statement that every $g$ can be written
$g=e\,\Delta\,e'$ with $e,e'$ products of elementary matrices and $\Delta$
diagonal; the displayed form follows because
$\Delta E_{ij}(a)\Delta^{-1}=E_{ij}(a\Delta_i\Delta_j^{-1})$ and
$\Delta_i\Delta_j^{-1}\in k^\times$, the elementary matrices being those
of the group $\mathrm{GL}_c(k)=\mathrm{GL}_{c,k}(k)$ of
[def-sc-general-linear-group].

For $c=1$ there is nothing to prove. Let $c\geq2$. First, left
multiplication by elementary matrices puts $g$ into upper triangular form:
if $g_{11}\neq0$, subtract $g_{i1}g_{11}^{-1}$ times row $1$ from row $i$
for each $i\geq2$, i.e. multiply on the left by
$\prod_{i\geq2}E_{i1}(-g_{i1}g_{11}^{-1})$; if $g_{11}=0$, then
$\det g\neq0$ gives $g_{i1}\neq0$ for some $i\geq2$, and multiplying on the
left by $E_{1i}(1)$ makes the $(1,1)$-entry equal to $g_{i1}\neq0$, after
which the previous step applies. Now clear the first row: right
multiplication by $E_{1j}(b)$ adds $b$ times column $1$ to column $j$, and
column $1$ vanishes below the diagonal, so choosing
$b=-g_{1j}g_{11}^{-1}$ makes the $(1,j)$-entry zero without destroying the
triangular shape ($j\geq2$). We have therefore found products $e_1,e_2$ of
elementary matrices with
$e_1ge_2=\begin{pmatrix}a&0\\0&A\end{pmatrix}$, $a=g_{11}\neq0$ and
$A\in\mathrm{GL}_{c-1}(k)$. By induction on $c$, $A=e_3\Delta'A'e_4$ with
$e_3,e_4$ products of elementary matrices of size $c-1$ (embedded in size
$c$) and $\Delta'$ diagonal; hence
$$
 g=e_1^{-1}\begin{pmatrix}1&0\\0&e_3\end{pmatrix}
 \begin{pmatrix}a&0\\0&\Delta'\end{pmatrix}
 \begin{pmatrix}1&0\\0&A'\end{pmatrix}e_2^{-1},
$$
a product of elementary matrices and one diagonal matrix as required.
