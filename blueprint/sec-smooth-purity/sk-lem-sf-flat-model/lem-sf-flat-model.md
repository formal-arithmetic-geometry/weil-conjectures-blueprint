+++
id = "lem-sf-flat-model"
kind = "lemma"
title = "Bounded flat model of finite Tor amplitude"
order = 2169
uses = ["def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "lem-exc-constant-inverse-image-flat"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\in\mathbf Z_{\geq1}$, and put $A=A_{E,n}$. Let $T$ be a scheme on
which $\ell$ is invertible, and let $K\in D^b_c(T,A)$ be a
bounded constructible
complex of $A_T$-modules on the
small pro-étale site. For
integers $a\leq b$ the following two conditions are equivalent.

1. **(i)** $K$ has finite Tor
amplitude in $[a,b]$: for every sheaf $M$ of $A_T$-modules placed in
degree zero one has $\mathcal H^r(K\otimes_A^LM)=0$ for every
$r\in\mathbf Z\setminus[a,b]$.
1. **(ii)** $K$ is isomorphic in $D(T_{\mathrm{proet}},A)$ to a bounded
complex $P$ of *flat* $A_T$-module sheaves with $P^q=0$ for
$q\notin[a,b]$, flatness meaning, as in
[lem-exc-constant-inverse-image-flat], that $P^q\otimes_A-$
preserves injections of $A_T$-module sheaves.

The same equivalence holds with the corresponding constructibility,
derived-tensor and Tor-amplitude conditions on a small étale site.

*Constructible variant.* If $T$ is Noetherian (for instance of finite type
over $k$) and $K\in D^b_c(T_{\Et},A)$ on the small étale site has finite Tor
amplitude in $[a,b]$, then $K$ is isomorphic in $D(T_{\Et},A)$ to a bounded
complex $P$ of flat *constructible* $A_T$-module sheaves with $P^q=0$ for
$q\notin[a,b]$; in particular every object of $D^b_{ctf}(T_{\Et},A)$ has such
a model. The key input is that every constructible sheaf of $A$-modules on
$T_{\Et}$ is a quotient of a finite direct sum of sheaves $j_{V!}A_V$ with
$j_V:V\to T$ étale and $V$ affine,
and that kernels and cokernels of maps of constructible sheaves of
$A$-modules are constructible.
