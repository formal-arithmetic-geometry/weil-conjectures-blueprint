+++
id = "prop-sf-localization-all-stages"
kind = "theorem"
title = "The closed-support triangle at every coefficient stage"
order = 2208
tags = ["latex:proposition"]
uses = ["def-sc-etale-torsion-cd", "def-weil-algebraically-closed-coefficients", "def-weil-derived-complete", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-inverse-image", "def-weil-finite-tor-amplitude", "def-weil-pbc-proetale-operations", "def-weil-rationalization-karoubi", "def-weil-weil-sheaf-complex", "lem-exc-proetale-closed-essential-image", "lem-exc-proetale-closed-exact", "lem-exc-proetale-closed-support", "lem-exc-proetale-support-triangle", "lem-exc-residue-tor-test", "lem-sf-etale-direct-image-vanishing", "lem-sf-proetale-constructible-origin", "lem-sf-proetale-residue-tor-test", "lem-sf-triangle-two-out-of-three", "lemma-weil-pbc-completed-pullback-reduction", "prop-sf-closed-immersion-unit", "prop-sf-closed-unit-all-stages", "prop-sf-open-closed-triangle-all-stages", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-descent-functors", "prop-weil-pbc-direct-image-limits", "prop-weil-pbc-proetale-constant-ring-map", "prop-weil-pbc-rational-transport", "prop-weil-pbc-roos-triangle", "prop-weil-pbc-scalar-extension", "thm-constructible-serre", "thm-fin-open-immersion", "thm-sc-finite-type-torsion-cd", "thm-sp-truncation-e2", "thm-weil-pbc-site-comparison", "thm-weil-pbc-verdier-axioms"]
+++
Let $X$ be a separated finite-type $k$-scheme, let $i:Z\hookrightarrow X$ be
a closed immersion and $j:U\hookrightarrow X$ the complementary open
immersion. Let $\Lambda$ be one of the coefficient stages
$A_{E,n},\mathcal O_E,E,\Qlb$, with the categories $D^b_c(-,\Lambda)$ of
[def-weil-derived-complete-integral-detailed],
[def-weil-rationalization-karoubi],
[def-weil-algebraically-closed-coefficients], the pullbacks of
[def-weil-derived-pullback-tensor-hom] and the direct images $i_*$, $Rj_*$
of [def-weil-derived-direct-image].

1. $Rj_*$ carries $D^b_c(U,\Lambda)$ into $D^b_c(X,\Lambda)$.
2. $i_*:D^b_c(Z,\Lambda)\to D^b_c(X,\Lambda)$ has a right adjoint $Ri^!$;
   it is the exceptional inverse image of
   [def-weil-exceptional-inverse-image] (at $\mathcal O_E$ it is
   $R\varprojlim_n\operatorname{Res}_nRi_n^!K_n$, with reductions
   $Ri_n^!K_n$).
3. For $K\in D^b_c(X,\Lambda)$ the closed exceptional counit and the open
   unit extend to a distinguished triangle
   $$
   i_*Ri^!K\longrightarrow K\longrightarrow Rj_*j^*K
   \longrightarrow i_*Ri^!K[1],
   $$
   with $\operatorname{Hom}(i_*Ri^!K[m],Rj_*j^*K)=0$ for all $m$, so the
   third arrow is unique and the triangle is functorial in $K$.
4. $Ri^!Rj_*G=0$ for $G\in D^b_c(U,\Lambda)$, and the unit
   $Q\to Ri^!i_*Q$ is an isomorphism for $Q\in D^b_c(Z,\Lambda)$.

The same holds on the finite-Tor subcategories $D^b_{ctf}(-,\Lambda)$ of
[def-weil-finite-tor-amplitude]. Let $d=\dim U$ and assume
$c=\operatorname{cd}_{\rm tor}(k)$ ([def-sc-etale-torsion-cd]) is finite
($c=0$ for $k$ algebraically closed).

- (1') $Rj_*$ carries $D^b_{ctf}(U,\Lambda)$ into $D^b_{ctf}(X,\Lambda)$;
   at $\Lambda=A_{E,n}$ Tor amplitude in $[a,b]$ goes to Tor amplitude in
   $[a,b+2d+c]$, and at $\mathcal O_E$ the same holds for the uniform
   interval of the reductions.
- (2') $Ri^!$ carries $D^b_{ctf}(X,\Lambda)$ into $D^b_{ctf}(Z,\Lambda)$,
   with Tor amplitude $[a,b]$ going to $[a,b+2d+c+1]$ (at $A_{E,n}$, and
   uniformly in the reductions at $\mathcal O_E$).
- (3') $i_*$, $i^*$ and $j^*$ preserve $D^b_{ctf}$ and Tor amplitude
   intervals; hence for $K\in D^b_{ctf}(X,\Lambda)$ all three vertices of
   the triangle of (3) lie in $D^b_{ctf}$.
- (4') For $G\in D^b_{ctf}(U,\Lambda)$ and $Q\in D^b_{ctf}(Z,\Lambda)$,
   $Ri^!Rj_*G=0$ and $Q\xrightarrow{\sim}Ri^!i_*Q$ inside $D^b_{ctf}$.

At $E$ and $\Qlb$ these are (1)–(4), since there $D^b_{ctf}=D^b_c$.

If $X,Z,U$ come from $k_0$-schemes and $\Lambda\in\{E,\Qlb\}$, then $Ri^!$
carries Weil structures ([def-weil-weil-sheaf-complex]) for which the
adjunction is equivariant, and for Weil complexes the three arrows of the
triangle and the unit are Weil-equivariant.
