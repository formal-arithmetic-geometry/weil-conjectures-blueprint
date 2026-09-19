+++
id = "def-finite-tor-amplitude"
kind = "definition"
title = "Finite Tor amplitude"
order = 25
uses = ["def-qbar-coefficient-category", "def-weil-derived-complete-integral", "def-weil-finite-coefficient-datum", "def-weil-finite-torsion-constructible", "def-weil-rational-coefficients"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For $n\geq1$, an object

$$
K\in D^b_c\bigl(Y,\mathcal O_E/\varpi_E^n\bigr)
$$

has *finite Tor amplitude* if there are
integers $a\leq b$ such that, for every sheaf $M$ of
$(\mathcal O_E/\varpi_E^n)_Y$-modules placed in degree zero,

$$
\mathcal H^r\!\left(
K\otimes^L_{(\mathcal O_E/\varpi_E^n)_Y}M\right)=0
\qquad\text{for }r\notin[a,b].
$$

For $\Lambda=\mathcal O_E$, define finite Tor amplitude to mean that every
finite reduction has finite Tor amplitude in this sense, with one interval
independent of $n$. Write
$D^b_{ctf}(Y,\Lambda)$ for the resulting full triangulated subcategory.
For field coefficients, define instead

$$
D^b_{ctf}(Y,E)=D^b_c(Y,E),
\qquad
D^b_{ctf}(Y,\Qlb)=D^b_c(Y,\Qlb).
$$

For integral coefficients and for
$\mathcal O_E/\varpi_E^n$, finite Tor amplitude is an additional condition
and is never inferred merely from bounded constructibility.
