+++
kind  = "proof"
of    = "sk-prop-av-isogeny-degree"
uses = ["sk-def-av-group-scheme", "sk-prop-av-pqf-finite"]
+++
$f$ is proper ($A$ is proper) and its fibres become translates $x+K$ of
the finite kernel after extending the residue field (see below), hence
are finite; so $f$ is finite by [sk-prop-av-pqf-finite]. All fibres
have the same length $d$. Here one must pass to a geometric fibre
first: the fibre $f^{-1}(y)$ over a point $y\in B$ need not have a
$\kappa(y)$-point, so it need not be isomorphic to $K$ over $\kappa(y)$
(for $[n]$ on an elliptic curve the generic fibre is the spectrum of a
degree-$n^2$ field extension of $\kappa(\eta)$). Let
$\Omega\supseteq\kappa(y)$ be an algebraically closed field. The
nonempty finite $\kappa(y)$-scheme $f^{-1}(y)$ has an $\Omega$-point
$x$, i.e. $x\in A(\Omega)$ with $f(x)=y_\Omega$, and translation by $x$
is an isomorphism of $\Omega$-schemes
$K_\Omega\xrightarrow{\sim}f_\Omega^{-1}(y_\Omega)
=f^{-1}(y)\times_{\kappa(y)}\Omega$. Hence
$\dim_{\kappa(y)}\Gamma(f^{-1}(y),\cO)
=\dim_\Omega\Gamma(f^{-1}(y)\times_{\kappa(y)}\Omega,\cO)
=\dim_\Omega(\cO_K\otimes_k\Omega)=d$, the fibre length being
unchanged by the field extension $\kappa(y)\subseteq\Omega$. Since $B$ is reduced and
the coherent sheaf $f_*\cO_A$ has fibre dimension
$\dim_{\kappa(y)}(f_*\cO_A\otimes\kappa(y))=d$ at every point $y$,
Nakayama's lemma shows that $f_*\cO_A$ is locally free of rank $d$;
hence $f$ is flat.
