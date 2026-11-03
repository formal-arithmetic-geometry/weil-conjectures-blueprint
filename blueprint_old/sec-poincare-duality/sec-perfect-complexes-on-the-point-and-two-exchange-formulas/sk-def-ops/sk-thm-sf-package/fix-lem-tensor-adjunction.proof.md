+++
kind  = "proof"
of    = "fix-lem-tensor-adjunction"
uses = ["def-weil-derived-pullback-tensor-hom", "fix-prop-adjunctions", "fix-prop-projection-formula", "lemma-weil-pbc-geometric-stalk-conservative", "sk-prop-scalar-six", "sk-lem-integral-models", "det-lem-coefficient-finite-descent-objects"]
+++
Step 1: the construction. For every
$L\in D^b_{ctf}(Y,\Lambda)$, the derived tensor–internal-Hom
adjunction of [def-weil-derived-pullback-tensor-hom] and the
adjunction of [fix-prop-adjunctions] give the chain

$$
\begin{aligned}
\Hom_Y\bigl(L,R\mathcal Hom_Y(Rf_!M,N)\bigr)
&\cong\Hom_Y(Rf_!M\otimes^L_{\Lambda}L,N)\\
&\cong\Hom_Y\bigl(Rf_!(M\otimes^L_{\Lambda}Lf^*L),N\bigr)\\
&\cong\Hom_X\bigl(M\otimes^L_{\Lambda}Lf^*L,f^!N\bigr)\\
&\cong\Hom_X\bigl(Lf^*L,R\mathcal Hom_X(M,f^!N)\bigr)\\
&\cong\Hom_Y\bigl(L,Rf_*R\mathcal Hom_X(M,f^!N)\bigr),
\end{aligned}
$$

where the second isomorphism is the inverse of the projection formula
of [fix-prop-projection-formula] (applicable since $M$ and
$L$ lie in the finite-Tor subcategories), and the first, third, and
fourth are the tensor–internal-Hom adjunction of
[def-weil-derived-pullback-tensor-hom] with the adjunction
$Rf_!\dashv Rf^!$ of [fix-prop-adjunctions], the last being
the adjunction $Lf^*\dashv Rf_*$ of
[fix-prop-adjunctions]. Step 2: detection. The adjunction chain is natural in
$L\in D^b_{ctf}(Y,\Lambda)$, so it defines a canonical map of the two
objects of $D(Y_{\mathrm{pro\acute et}},\Lambda)$, for every admissible
condensed $\Lambda$. To see that it is an isomorphism, take
$L=e_!\Lambda_V[r]$, where $e:V\to Y$ is a quasi-compact étale map and
$r\in\mathbf Z$. Such an extension by zero lies in $D^b_{ctf}(Y,\Lambda)$,
so it is in the domain used in step 1, and the resulting Hom groups are the
cohomology groups of the two objects on $V$. Hence the cone $C$ satisfies
$H^r(V,C)=0$ for every quasi-compact étale $V\to Y$ and every $r$. For finite
$\Lambda$ the objects are classical, and conservativity of geometric stalks
([lemma-weil-pbc-geometric-stalk-conservative]) shows $C=0$, without first
assuming that either output belongs to the finite-Tor subcategory.

For $\Lambda=\mathcal O_E,E,\Qlb$ write $\phi_{M,N}$ for the map of Step 1.
Both of its sides are values of the exact functors
$Rf_*R\mathcal Hom_X(M,Rf^!(-))$ and $R\mathcal Hom_Y(Rf_!M,-)$ on $N$, and of
the exact contravariant functors $Rf_*R\mathcal Hom_X(-,f^!N)$ and
$R\mathcal Hom_Y(Rf_!(-),N)$ on $M$. Every map in the chain of Step 1 is a
composite of units, counits and evaluation maps of the adjunctions and of the
projection formula, and the coefficient comparison maps of
[sk-prop-scalar-six] for $f^*$, $Rf_*$, $Rf_!$, $f^!$, $\otimes^L$ and
$R\mathcal Hom$ are isomorphisms on $D^b_{ctf}$ that respect these maps. Hence,
for every coefficient map $\Lambda\to\Lambda'$ of [sk-prop-scalar-six], the
comparison maps identify $(\phi_{M,N})_{\Lambda'}$ with
$\phi_{M_{\Lambda'},N_{\Lambda'}}$; this is the asserted compatibility with
finite reduction and scalar extension.

*$\Lambda=\mathcal O_E$.* Both objects are derived complete, and by the
compatibility just proved the reduction of $\phi_{M,N}$ modulo $\pi_E$ is
$\phi$ for the finite ring $A_{E,1}=\mathcal O_E/\pi_E$, an isomorphism by the
finite case. So $C\otimes^L_{\mathcal O_E}\mathcal O_E/\pi_E=0$, and derived
Nakayama gives $C=0$.

*$\Lambda=E$.* The map $\phi_{M,N}$ is natural in $M$ and $N$ and compatible
with shifts, so for fixed $N$ a distinguished triangle $M'\to M\to M''\to$ in
$D^b_{ctf}(X,E)$ gives a morphism of distinguished triangles between the two
sides, and likewise in $N$. Therefore the pairs $(M,N)$ for which $\phi_{M,N}$
is an isomorphism form, in each variable, a class closed under shifts,
isomorphisms and cones. By [sk-lem-integral-models] (4) every object of
$\Dbc(X,E)=D^b_{ctf}(X,E)$ is obtained by finitely many cones and shifts from
objects $(a_!L_0)[1/\ell]=(a_!L_0)_E$ with $a_!L_0\in D^b_{ctf}(X,\mathcal O_E)$
([sk-lem-integral-models], first paragraph and (3)), and likewise on $Y$. So it
suffices to treat $M=(M_0)_E$ and $N=(N_0)_E$ with $M_0\in
D^b_{ctf}(X,\mathcal O_E)$ and $N_0\in D^b_{ctf}(Y,\mathcal O_E)$. Then
$\phi_{M,N}$ is identified with $(\phi_{M_0,N_0})_E$, which is an isomorphism
by the case $\mathcal O_E$.

*$\Lambda=\Qlb$.* By [det-lem-coefficient-finite-descent-objects] there are a
finite $E/\Ql$ and models $M_E\in\Dbc(X,E)$, $N_E\in\Dbc(Y,E)$ with
$(M_E)_{\Qlb}\cong M$ and $(N_E)_{\Qlb}\cong N$: a model over $E$ extends to a
model over every finite $F\supseteq E$, so one $E$ serves for both. Since
$\phi$ is natural, $\phi_{M,N}$ is isomorphic to
$\phi_{(M_E)_{\Qlb},(N_E)_{\Qlb}}$, which is identified with
$(\phi_{M_E,N_E})_{\Qlb}$, an isomorphism by the case $E$.

The same Yoneda argument directly in
$D(Y_{\mathrm{pro\acute et}},\Lambda)$ is the one of [sk-thm-sf-tensor-hom].
Naturality follows by transposing it to the same tensor and counit
composites. This asserts compatibility of
the specified maps; it does not supply a separate internal-Hom reduction
isomorphism outside the domains where that comparison has been proved.
