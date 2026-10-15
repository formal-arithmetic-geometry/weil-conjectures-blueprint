+++
id = "sk-def-exchange"
kind = "definition"
title = "Derived exchange"
order = 1044
lean = ["AlgebraicGeometry.Etale.baseChange"]
uses = ["sk-def-conv", "sk-def-pbc-conventions"]
tags = ["sketch"]
+++
Consider a cartesian square

$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{g} & Y.
\end{array}
$$

The commutativity of the square supplies the canonical composition
isomorphism of functors $\Sh(Y_{\Et})\to\Sh(X'_{\Et})$

$$
\theta_\square:f'^{-1}g^{-1}\xrightarrow{\ \sim\ }g'^{-1}f^{-1}.
$$

Since inverse images are exact, $\theta_\square$ also denotes the induced
isomorphism of functors $D^+(Y_{\Et},\Lambda)\to D^+(X'_{\Et},\Lambda)$. (For
$F\in\Sh(X_{\Et})$ the *underived exchange map*
$\Ex^0_{\square,F}:g^{-1}f_*F\to f'_*g'^{-1}F$ in $\Sh(Y'_{\Et})$ is the
adjoint, under $f'^{-1}\dashv f'_*$, of
$f'^{-1}g^{-1}f_*F\xrightarrow{\theta_\square}g'^{-1}f^{-1}f_*F
\xrightarrow{g'^{-1}\varepsilon_f}g'^{-1}F$, with $\varepsilon_f$ the counit;
it is natural in $F$, and likewise for sheaves of $\Lambda$-modules.)

**Definition (derived exchange).** For $K\in D^+(X_{\Et},\Lambda)$, the
*exchange morphism*

$$
\Ex_{\square,K}:g^{-1}Rf_*K\longrightarrow Rf'_*g'^{-1}K
\qquad\text{in }D^+(Y'_{\Et},\Lambda)
$$

is the adjoint, under $f'^{-1}\dashv Rf'_*$, of

$$
f'^{-1}g^{-1}Rf_*K\xrightarrow{\ \theta_\square\ }g'^{-1}f^{-1}Rf_*K
\xrightarrow{\ g'^{-1}\varepsilon_f\ }g'^{-1}K
\qquad\text{in }D^+(X'_{\Et},\Lambda),
$$

where $\varepsilon_f:f^{-1}Rf_*\to\mathrm{id}$ now denotes the derived counit
on $D^+(X_{\Et},\Lambda)$. The morphism is natural in $K$, so
$\Ex_\square:g^{-1}Rf_*\to Rf'_*g'^{-1}$ is a natural transformation of
functors $D^+(X_{\Et},\Lambda)\to D^+(Y'_{\Et},\Lambda)$.

The derived adjunction exists because inverse image is exact and its right
adjoint preserves injectives. The construction needs only a commutative
square; the cartesian hypothesis matters for the question whether it is an
isomorphism. Concretely, for a bounded below injective resolution
$K\to I^\bullet$ and an injective replacement $g'^{-1}I^\bullet\to J^\bullet$,
the exchange is represented by the morphism of complexes
$g^{-1}f_*I^\bullet\xrightarrow{\Ex^0_{\square,I^\bullet}}f'_*g'^{-1}I^\bullet
\to f'_*J^\bullet$, independently of the choices.
