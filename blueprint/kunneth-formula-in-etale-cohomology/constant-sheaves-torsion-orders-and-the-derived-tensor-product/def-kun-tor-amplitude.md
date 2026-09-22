+++
id = "def-kun-tor-amplitude"
kind = "definition"
title = "Tor amplitude"
order = 6028
lean = ["AlgebraicGeometry.Etale.HasTorAmplitude"]
uses = ["def-kun-derived-tensor"]
+++
Let $T$ be a scheme, $\Lambda$ a commutative ring, and
$E\in D(T_{\Et},\Lambda)$, $a,b\in\mathbf Z$. The object $E$ has *tor
amplitude in $[a,b]$* (resp. $[a,\infty)$) if for every sheaf
$\mathcal M\in\Mod(T_{\Et},\Lambda)$ placed in degree zero,
$$
H^i\bigl(E\otimes^{\mathbf L}_\Lambda\mathcal M\bigr)=0
\qquad\text{for all }i\notin[a,b]\ \ (\text{resp. }i<a).
$$

That a bounded complex of flat $\Lambda_T$-module sheaves supported in
degrees $[a,b]$ has tor amplitude in $[a,b]$ is
[lem-kun-flat-bounded-tor-amplitude]; boundedness alone does not imply
finite tor amplitude.
