+++
id = "def-exceptional-inverse-image"
kind = "definition"
title = "Exceptional inverse image notation"
order = 55
uses = ["def-all-coefficient-compact-support", "def-exceptional-adjoint-admissible", "def-weil-finite-coefficient-datum", "thm-qbar-functor-descent"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum]. Let
$f:X\to Y$ be separated and of finite type. For every $n\geq1$, at a finite stage at which
$f$ is exceptional-adjoint admissible, set

$$
Rf_n^!=Rf_n^{\times}|_{D^b_c(Y,\mathcal O_E/\varpi_E^n)}:
D^b_c\bigl(Y,\mathcal O_E/\varpi_E^n\bigr)
\longrightarrow D^b_c\bigl(X,\mathcal O_E/\varpi_E^n\bigr).
$$

For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$, at a stage at which $f$ is
admissible, the compatible finite-reduction right adjoints, followed
respectively by derived inverse limit, rationalization, or the common-stage
construction, define

$$
Rf^!:D^b_c(Y,\Lambda)\longrightarrow D^b_c(X,\Lambda).
$$

At finite level, for
$K\in D^b_c(X,\mathcal O_E/\varpi_E^n)$ and
$L\in D^b_c(Y,\mathcal O_E/\varpi_E^n)$, this right adjoint is
characterized by

$$
\Hom_Y(Rf_{!,n}K,L)\cong\Hom_X(K,Rf_n^!L).
$$

For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$, every
$K\in D^b_c(X,\Lambda)$, and every $L\in D^b_c(Y,\Lambda)$, the
higher-coefficient right adjoint is characterized by

$$
\Hom_Y(Rf_!K,L)\cong\Hom_X(K,Rf^!L).
$$

Its restriction to finite-Tor objects is part of admissibility. Smooth
purity and Poincare duality for smooth proper structure morphisms are stated
independently below.
