+++
kind  = "proof"
of    = "fix-lem-tensor-adjunction"
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
assuming that either output belongs to the finite-Tor subcategory. For
$\Lambda=\mathcal O_E,E,\Qlb$ the two objects are, by construction, values of
the exact functors $Rf_*R\mathcal Hom_X(M,Rf^!(-))$ and
$R\mathcal Hom_Y(Rf_!M,-)$ on $N$, both of which commute with reduction
modulo $\pi_E$ and with extension of scalars ([sk-prop-scalar-six]); for
$\mathcal O_E$ both objects are derived complete, and the reduction of the map
modulo $\pi_E$ is the map for the finite ring $A_{E,1}$, so derived Nakayama
gives $C=0$; for $E$ one reduces to integral generators, and for $\Qlb$ to a
finite $E$. The same Yoneda argument directly in
$D(Y_{\mathrm{pro\acute et}},\Lambda)$ is the one of [sk-thm-sf-tensor-hom].
Naturality and the comparison squares under reduction follow by transposing
them to the same tensor and counit composites. This asserts compatibility of
the specified maps; it does not supply a separate internal-Hom reduction
isomorphism outside the domains where that comparison has been proved.
