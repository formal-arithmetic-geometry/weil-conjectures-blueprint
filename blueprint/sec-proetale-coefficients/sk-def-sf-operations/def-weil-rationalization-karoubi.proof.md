+++
kind  = "proof"
of    = "def-weil-rationalization-karoubi"
uses = ["sk-prop-sfb-cartesian-coefficients", "sk-prop-sfb-qlbar-colimit-x"]
+++
The equivalence is [sk-thm-sfb-rationalization-comparison], applied to the integral category
of [def-weil-derived-complete-integral-detailed]. That category is $\Dbc(Y,\mathcal O_E)$ in
the condensed sense, by the comparison recorded there.

It remains to see that the two descriptions of $-\otimes_EL$ agree. Let
$K\in D^b_c(Y,\mathcal O_E)$. The ring $\mathcal O_{L,Y}$ is a finite free
$\mathcal O_{E,Y}$-module ([sk-prop-sfb-cartesian-coefficients] (2)). Hence
$\mathcal O_{L,Y}\otimes^L_{\mathcal O_{E,Y}}K$ is a finite direct sum of copies of $K$ as an
$\mathcal O_{E,Y}$-complex, so it is derived $\varpi_E$-complete. It is then also derived
$\varpi_L$-complete, since $\varpi_E$ is a unit times a power of $\varpi_L$. The completion
in the levelwise recipe therefore changes nothing, and that recipe computes
$\mathcal O_{L,Y}\otimes^L_{\mathcal O_{E,Y}}K$. Inverting $\ell$ gives

$$
 L_Y\otimes_{\mathcal O_{L,Y}}\bigl(\mathcal O_{L,Y}\otimes^L_{\mathcal O_{E,Y}}K\bigr)
 \cong L_Y\otimes^L_{\mathcal O_{E,Y}}K
 \cong L_Y\otimes_{E_Y}\bigl(E_Y\otimes_{\mathcal O_{E,Y}}K\bigr).
$$

Here $L_Y=\mathcal O_{L,Y}[1/\ell]$ and $E_Y=\mathcal O_{E,Y}[1/\ell]$
([sk-prop-sfb-qlbar-colimit-x]), and these extensions of scalars are exact. So the
integral recipe corresponds to $L_Y\otimes_{E_Y}-$ under the identification of the
statement.
