+++
id = "det-pbc-complete-exchange-map"
kind = "definition"
title = "The completed exchange map"
order = 2043
lean = ["AlgebraicGeometry.ProEtale.derivedBaseChangeMap", "AlgebraicGeometry.ProEtale.completedDerivedBaseChangeMap"]
uses = ["det-pbc-complete-derived-completion", "lemma-weil-pbc-completed-pullback-reduction", "prop-weil-pbc-direct-image-limits"]
+++
Consider a commutative square of schemes

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle p'}\downarrow & & \downarrow{\scriptstyle p}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
$$

and use the notation of [det-pbc-complete-derived-completion] (for instance
$R=\mathcal O_E$, $\varpi=\pi_E$).

1. *Base change morphism.* For $M\in D(X)$, the base change morphism
   $\operatorname{Ex}_M\colon g^*Rp_*M\to Rp'_*g'^*M$ is the mate of the
   pullback comparison $p'^*g^*\simeq g'^*p^*$ of the square under the
   adjunctions $p^*\dashv Rp_*$ and $p'^*\dashv Rp'_*$ of derived inverse and
   direct images: the composite of the unit of $p'^*\dashv Rp'_*$, the pullback
   comparison and the counit of $p^*\dashv Rp_*$.
2. *Completed exchange map.* For $K\in D(X)$, the *completed exchange map*
   $$
   \operatorname{Ex}^{\mathrm{comp}}_K\colon g^*_{\mathrm{comp}}Rp_*K\longrightarrow
   Rp'_*g'^*_{\mathrm{comp}}K
   $$
   between the completed inverse images of
   [lemma-weil-pbc-completed-pullback-reduction] is the unique morphism whose
   composite with the completion map $g^*Rp_*K\to g^*_{\mathrm{comp}}Rp_*K$ is
   $$
   g^*Rp_*K\xrightarrow{\operatorname{Ex}_K}Rp'_*g'^*K
   \xrightarrow{Rp'_*(\kappa_{g'^*K})}Rp'_*g'^*_{\mathrm{comp}}K;
   $$
   it exists and is unique because $Rp'_*g'^*_{\mathrm{comp}}K$ is derived
   complete [prop-weil-pbc-direct-image-limits] and the derived completion is
   left adjoint to the inclusion of derived complete objects
   [det-pbc-complete-derived-completion].

The completed exchange map is natural in $K$, being built from natural
transformations, and it is defined for every $K\in D(X)$.
