+++
id = "def-verdier-duality-functor"
kind = "definition"
title = "Verdier duality functor"
order = 69
uses = ["def-derived-internal-hom", "def-exceptional-inverse-image", "def-weil-finite-coefficient-datum"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum], and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. For an exceptional-adjoint admissible
structure morphism
$a_Y:Y\to\Spec k$, define

$$
\omega_Y:=Ra_Y^!\Lambda\in D^b_c(Y,\Lambda),
\qquad
D_YK:=R\mathcal Hom_{\Lambda_Y}(K,\omega_Y)
\qquad\bigl(K\in D^b_{ctf}(Y,\Lambda)\bigr).
$$

At finite level $\Lambda_Y=(\mathcal O_E/\varpi_E^n)_Y$; at integral and
rational level it is $\widehat{\mathcal O}_{E,Y}$ and $E_Y$; the
$\Qlb$-object is represented over a common finite field.
