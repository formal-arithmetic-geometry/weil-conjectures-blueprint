+++
id = "prop-ramified-coefficient-change"
kind = "theorem"
title = "Ramified coefficient change and cofinal reindexing"
order = 16
tags = ["latex:proposition"]
uses = ["def-finite-reduction", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients", "thm-rational-lattice-localization"]
+++
For a scheme $Y$, fix a prime $\ell\neq p$, an algebraic closure
$\Qlb/\Ql$, and finite extensions $E\subset L$ inside $\Qlb$, with
valuation rings $\mathcal O_E\subset\mathcal O_L$ and uniformizers
$\varpi_E,\varpi_L$. Let $e$ be the ramification index of $L/E$. If
$K\in D^b_c(Y,E)$ and
$K_{\mathcal O_E}\in D^b_c(Y,\mathcal O_E)$ is an integral lattice for
$K$, its completed scalar
extension is

$$
K_{\mathcal O_E}\widehat\otimes^L_{\mathcal O_E}\mathcal O_L
:=R\varprojlim_n\left(
K_{\mathcal O_E}\otimes^L_{\widehat{\mathcal O}_{E,Y}}
(\mathcal O_L/\varpi_E^n\mathcal O_L)_Y\right).
$$

Because $\varpi_E\mathcal O_L=u\varpi_L^e\mathcal O_L$ for a unit
$u$, the subsystems indexed by $\varpi_E^n\mathcal O_L$ and by
$\varpi_L^m\mathcal O_L$ are cofinal. Their derived inverse limits are
canonically isomorphic. After inverting either uniformizer, this object
represents $K\otimes^L_{E_Y}L_Y$, independently of the lattice. For
every further finite extension $L\subset M\subset\Qlb$, these
isomorphisms satisfy the tower equation for $E\subset L\subset M$.
