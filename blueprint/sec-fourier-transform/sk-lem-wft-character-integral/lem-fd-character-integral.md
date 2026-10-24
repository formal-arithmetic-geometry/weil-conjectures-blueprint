+++
id = "lem-fd-character-integral"
kind = "lemma"
title = "The integral of a linear character"
order = 3942
uses = ["def-fd-artin-schreier-sheaf", "lem-wft-as-comparison", "lem-fd-as-cover-affine-line", "lem-fd-as-characters", "lem-fd-finite-pushforward-cohomology", "thm-pur-vector-bundle-thom", "lem-wft-kunneth-compatibilities", "sk-prop-sfb-finite-extension-compatibility"]
+++
Let $\psi:k_0\to\Lambda^\times$ be a nontrivial additive character, with
$\Lambda=E\supset\mu_p$ or $\Lambda=\overline{\mathbf Q}_\ell$, let $\Omega$ be
an algebraically closed field containing $k_0$, and let
$\lambda:\mathbf A^r_\Omega\to\mathbf A^1_\Omega$ be a linear form. Write
$\lambda^*\mathcal L_\psi$ for the pullback of the Artin–Schreier sheaf of
[def-fd-artin-schreier-sheaf] along $\mathbf A^r_\Omega\xrightarrow{\lambda}
\mathbf A^1_\Omega\to\mathbf A^1_{k_0}$. Then

$$
 R\Gamma_c(\mathbf A^r_\Omega,\lambda^*\mathcal L_\psi)
 \simeq
 \begin{cases}
 \Lambda(-r)[-2r],&\lambda=0,\\
 0,&\lambda\ne0,
 \end{cases}
$$

where for $\lambda=0$ (so $\lambda^*\mathcal L_\psi=\Lambda$, trivialized by
[lem-wft-as-unit-trivialization]) the isomorphism is the vector-bundle trace
$\operatorname{tr}:R\Gamma_c(\mathbf A^r_\Omega,\Lambda)(r)[2r]\to\Lambda$ of
[thm-pur-vector-bundle-thom] for the trivial bundle over $\operatorname{Spec}\Omega$.
