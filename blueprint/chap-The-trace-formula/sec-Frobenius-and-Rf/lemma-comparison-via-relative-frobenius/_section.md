+++
id = "lemma-comparison-via-relative-frobenius"
kind = "lemma"
title = "Comparison via relative Frobenius"
order = 1000
lean = ["AlgebraicGeometry.isFinite_relativeFrobenius", "AlgebraicGeometry.isUniversalHomeomorphism_relativeFrobenius", "AlgebraicGeometry.isFinite_and_isUniversalHomeomorphism_relativeFrobenius", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriekFrobeniusComparison", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriekFrobeniusComparison_add", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriekFrobeniusCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.frobeniusCoefficientIterate_lowerShriekFrobeniusCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.frobeniusCompactOperator_lowerShriekFrobeniusCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.stalk_lowerShriekFrobeniusCoefficient_iterate"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-composition-base-change-rf-shriek", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-frobenius-correspondences-their-operators", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $f_0:X_0\to Y_0$ be a morphism of separated schemes of finite
type over $k_0$, write $f:X\to Y$ for its geometric base change, and
let $m\geq1$. Put

$$
X'_m=Y\times_{\Phi_Y^m,Y,f}X,
\quad p_m:X'_m\to X,\quad f'_m:X'_m\to Y,
\quad r_m=(f,\Phi_X^m):X\to X'_m,
$$

where $p_m$ and $f'_m$ are the two projections.

1. The relative Frobenius $r_m$ is a finite universal homeomorphism,
   $p_mr_m=\Phi_X^m$ and $f'_mr_m=f$, and there are natural isomorphisms
   $$
   \begin{aligned}
   \theta_{f,m}:(\Phi_Y^m)^*Rf_!K
   &\simeq Rf'_{m!}p_m^*K
   \xrightarrow{Rf'_{m!}\eta_{r_m}}
   Rf'_{m!}Rr_{m*}r_m^*p_m^*K\\
   &\simeq Rf_!(\Phi_X^m)^*K,
   \end{aligned}
   $$
   compatible with iteration in $m$.
2. For a Frobenius correspondence $\psi:\Phi_X^*K\to K$ on
   $K\in D^b_{\mathrm{ctf}}(X,A)$, the object $L=Rf_!K$ of $D^b_{\mathrm{ctf}}(Y,A)$ carries the
   Frobenius correspondence $\psi'=Rf_!\psi\circ\theta_{f,1}:\Phi_Y^*L\to L$,
   and its iterates are
   $$
   \psi'_m=Rf_!\psi_m\circ\theta_{f,m}.
   $$
3. The composition isomorphism
   $R\Gamma_c(Y,L)\simeq R\Gamma_c(X,K)$ intertwines the
   endomorphisms $T_{c_m}(\psi'_m)$ on $Y$ and $T_{c_m}(\psi_m)$ on
   $X$ of Definition [definition-frobenius-correspondences-their-operators].
4. At $y\in Y_0(\mathbf F_{q^m})$, base change for compact supports
   identifies $(L_{\bar y},\psi'_{m,\bar y})$ with
   $$
   \left(R\Gamma_c(X_{\bar y},K|_{X_{\bar y}}),
   T_{c_1}(\psi_m|_{X_{\bar y}})\right),
   $$
   where the fibre is regarded as a scheme over $\mathbf F_{q^m}$, with
   the $q^m$-power Frobenius as its scheme Frobenius.
