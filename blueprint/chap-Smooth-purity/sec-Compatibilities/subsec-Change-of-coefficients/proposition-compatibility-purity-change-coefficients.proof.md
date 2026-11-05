+++
kind = "proof"
of = "proposition-compatibility-purity-change-coefficients"
order = 812
uses = ["proposition-sp-tower-geometric"]
+++
Both kinds of comparison maps are compatible with composition of coefficient
maps, so it suffices to treat the elementary maps in the list of
Proposition [proposition-six-operations-change-coefficients]. For a map
$A\to B$ of finite rings the assertion for $\gamma_f$ is
(9.17), and the assertion for the traces follows from
it and the counit identity (9.16). A continuous map
$\mathcal O_E\to A$ factors through $\mathcal O_E/\ell^n$ for some $n$, so it
suffices to treat $\mathcal O_E\to\mathcal O_E/\ell^n$. By construction
(Section [subsec-Integral-coefficients-2]), $\operatorname{red}_X$ carries
$\gamma_{f,\mathcal O_E}(K)$ to $\gamma_{f,\bullet}(\operatorname{red}_YK)$,
whose level $n$ is $\gamma_{f,\mathcal O_E/\ell^n}(K/\ell^n)$. Here the
targets are identified by the isomorphism
$\operatorname{red}_Xf^!_{\mathcal O_E}K\simeq f^!_\bullet\operatorname{red}_YK$,
whose level $n$ is an isomorphism
$(f^!_{\mathcal O_E}K)/\ell^n\simeq f^!_{\mathcal O_E/\ell^n}(K/\ell^n)$, and this
identification is the change-of-coefficients map of
Proposition [proposition-six-operations-change-coefficients]. Indeed,
the integral counit reduces to the finite one, namely to level $n$ of the
counit on towers (Section [subsec-Base-change-and-composition] and
Proposition [proposition-sp-tower-geometric]), and both maps are
transposes of that counit composed with the comparison for $Rf_!$. So this
case follows from the finite one. For $\mathcal O_E\to E$ and $E\to\overline{\mathbf Q}_\ell$
the assertion holds by construction, because $\gamma_{f,E}$ and
$\gamma_{f,\overline{\mathbf Q}_\ell}$ were defined by inverting $\ell$ in the integral adjunction
and by extension of scalars from finite extensions of $\mathbf Q_\ell$
(Section [subsec-Field-coefficients]). For a finite extension $F/E$ we showed before
Theorem [theorem-sp-qbar] that extension of scalars carries the pair of
towers for $\mathcal O_E$ to the pair for $\mathcal O_F$ by a counit-preserving
isomorphism. By applying $R\varprojlim$ and inverting $\ell$ we get the cases
$\mathcal O_E\to\mathcal O_F$ and $E\to F$. In every case the statement for
the traces follows from the one for $\gamma_f$, because the change-of-coefficients
maps for $Rf_!$ and $f^!$ are compatible with the counits.
