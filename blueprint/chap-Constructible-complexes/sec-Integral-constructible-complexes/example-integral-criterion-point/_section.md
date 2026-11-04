+++
id = "example-integral-criterion-point"
kind = "example"
title = "The criterion over a point"
order = 227
+++
On the spectrum of an algebraically closed field, take for $K$ the sheaf
attached to an $\mathcal O_E$-module. The computation is then one with
modules, and it shows where the uniform rate comes from. Resolving
$\mathcal O_E/\pi_E^e$ by $[\mathcal O_E\xrightarrow{\pi_E^e}\mathcal O_E]$ in
degrees $-1,0$ and reducing modulo $\pi_E$, we find

$$
\mathcal O_E\otimes^{\mathbf L}_{\mathcal O_E}\mathbf F_E=\mathbf F_E,
\qquad
\mathcal O_E/\pi_E^e\otimes^{\mathbf L}_{\mathcal O_E}\mathbf F_E
=\bigl[\mathbf F_E\xrightarrow{\,0\,}\mathbf F_E\bigr]
=\mathbf F_E\oplus\mathbf F_E[1]\quad(e\geq1),
$$

since $\pi_E^e$ becomes zero modulo $\pi_E$. For
$P=\mathcal O_E^r\oplus\bigoplus_{i=1}^s\mathcal O_E/\pi_E^{e_i}$ the
reduction $K_1$ has $H^0=\mathbf F_E^{r+s}$ and $H^{-1}=\mathbf F_E^s$. Thus
$H^{-1}(K_1)$ counts the cyclic torsion summands. For
$K=\bigoplus_{n\geq1}\mathcal O_E/\pi_E^n$ we get
$K_1=\bigoplus_{n\geq1}(\mathbf F_E\oplus\mathbf F_E[1])$. This is not
constructible, because its cohomology is an infinite-dimensional vector space in
degrees $0$ and $-1$. In other words, a constructible $K_1$ allows only finitely
many torsion summands. For $P$ the single power $\pi_E^{\max e_i}$ then kills all
the torsion, and this is the uniform rate.

The completeness hypothesis cannot be dropped either. The module $E$ is
$\pi_E$-divisible, so $E\otimes^{\mathbf L}\mathcal O_E/\pi_E^n=0$ for all
$n$. Hence $K_1=0$ is constructible, yet $E$ is not a finitely generated
$\mathcal O_E$-module. The criterion does not apply because $E$ is not derived
complete: its derived
completion $R\varprojlim_n(E\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$ is zero.
