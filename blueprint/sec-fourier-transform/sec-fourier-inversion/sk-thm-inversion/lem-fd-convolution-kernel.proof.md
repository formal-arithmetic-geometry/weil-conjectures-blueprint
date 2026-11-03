+++
kind  = "proof"
of    = "lem-fd-convolution-kernel"
uses = ["det-thm-sfb-shriek-base-change"]
+++
*Step 1 (the integrand).* On $V\times_SV^\vee\times_SV$, with points
$(x,y,z)$, the multiplicativity and the inverse formula of
[prop-kernel-lisse], [lem-fd-as-lisse] give

$$
r_{12}^*\mathcal K_\psi\otimes r_{23}^*\mathcal K_{\psi^{-1}}
\cong\mathcal L_{\psi,\langle x,y\rangle}\otimes\mathcal L_{\psi,-\langle z,y\rangle}
\cong\mathcal L_{\psi,\langle x-z,y\rangle}.
$$

*Step 2 (vanishing off the diagonal).* Let $(\bar x,\bar z)$ be a geometric
point of $V\times_SV$ over the geometric point $\bar s$ of $S$, with values in
an algebraically closed field $\Omega$. By compact-support base change
([det-thm-sfb-shriek-base-change]), as in [lem-fd-stalk-formula], the stalk
$C_{(\bar x,\bar z)}$ is
$R\Gamma_c(V^\vee_{\bar s},\lambda^*\mathcal L_\psi)$ for the linear form
$\lambda=\langle x-z,\ \cdot\ \rangle$ on the fibre
$V^\vee_{\bar s}\cong\mathbf A^r_\Omega$. If $x\ne z$, then $\lambda\neq0$
and this vanishes by [lem-fd-character-integral].

*Step 3 (localization).* Let $j:U\hookrightarrow V\times_SV$ be the open
complement of the closed diagonal $\Delta$. By Step 2 all stalks of
$j^*C$ vanish, so $j^*C=0$, and the localization triangle
$j_!j^*C\to C\to\Delta_*\Delta^*C$ of [sk-prop-sf-open-closed-triangle]
gives a canonical isomorphism $C\xrightarrow{\sim}\Delta_*\Delta^*C$.

*Step 4 (the restriction to the diagonal).* The base change of $r_{13}$
along $\Delta$ is the projection $q:V\times_SV^\vee\to V$, the pullback to
$V$ of the vector bundle $V^\vee$, and by compact-support base change
$\Delta^*C\cong Rq_!(\mathcal L_{\psi,\langle x-x,y\rangle})=Rq_!(\mathcal L_{\psi,0})$.
The unit trivialization of [lem-wft-as-unit-trivialization] identifies
$\mathcal L_{\psi,0}$ with $\Lambda$, compatibly with the identification of
Step 1, and the vector-bundle trace of [thm-pur-vector-bundle-thom] for the
rank-$r$ bundle $q$ gives $Rq_!\Lambda\cong\Lambda_V(-r)[-2r]$, with the
twist of [def-wf-tate-twist]. Together with Step 3 this is the first
isomorphism.

*Step 5 (the same character).* For $\mathcal K_\psi\ast\mathcal K_\psi$ the
integrand is $\mathcal L_{\psi,\langle x+z,y\rangle}$, so Steps 2–4 hold with
the diagonal replaced by the antidiagonal $\{x+z=0\}$, the image of $\Delta$
under $\operatorname{id}\times\iota'$, which gives the second isomorphism.
