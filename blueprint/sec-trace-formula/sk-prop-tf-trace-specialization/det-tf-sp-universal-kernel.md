+++
id = "det-tf-sp-universal-kernel"
kind = "lemma"
title = "Nearby cycles of the universal kernel"
order = 3601
uses = ["thm-trf-verdier-duality"]
+++
Let $S$ be a strictly henselian trait with special point $s$ and generic point $\eta$,
$A$ a finite commutative $\ell$-primary ring with $\ell$ invertible on $S$, $S_X=R\Psi_{X/S}$,
and let $\alpha$, $\beta$, $\chi$, $\mu$, $\theta$ be the pullback, exceptional and proper
exchanges, the lax tensor map and the dualizing map of nearby cycles. Let $X$ be a
separated finite-type $S$-scheme with projections $p_1,p_2:X\times_SX\to X$ and diagonal
$\Delta$, let $K\in\Dctf(X_\eta,A)$, $K'=S_XK$, $P_X=K\boxtimes\mathbb DK$ and
$P'_X=K'\boxtimes\mathbb DK'$. Write $\lambda_K:P_X\xrightarrow{\sim}\cHom_A(p_2^*K,p_1^!K)$
for the external-duality isomorphism ([thm-trf-verdier-duality]) and
$e_K:P_X\to R\Delta_*\omega_X$ for the diagonal evaluation, and similarly on the special
fibre. Assume that the external product comparison
$\Pi_{M,N}=\mu(\alpha_{p_1}\otimes\alpha_{p_2}):S_XM\boxtimes S_XN\to S_{X\times_SX}(M\boxtimes N)$
and the nearby duality map $\delta_K:S_X\mathbb DK\to\mathbb D(S_XK)$, the tensor–Hom adjoint
of $\theta_XS_X(\operatorname{ev})\mu_X$, are isomorphisms. Put

$$
 \rho=(1\boxtimes\delta_K)\circ\Pi_{K,\mathbb DK}^{-1}:S_{X\times_SX}P_X\xrightarrow{\sim}P_X',
$$

and let $\mathfrak h:S_{X\times_SX}\cHom_A(p_2^*K,p_1^!K)\to\cHom_A(p_{2s}^*K',p_{1s}^!K')$
be the tensor–Hom mate of $S(\operatorname{ev})\mu$, precomposed with $\alpha_{p_2}$ and
postcomposed with $\beta_{p_1}$. Then

$$
 \mathfrak h\,S(\lambda_K)=\lambda_{K'}\rho,
 \qquad
 e_{K'}\rho=R\Delta_{s*}\theta_X\,\chi_\Delta\,S(e_K).
$$
