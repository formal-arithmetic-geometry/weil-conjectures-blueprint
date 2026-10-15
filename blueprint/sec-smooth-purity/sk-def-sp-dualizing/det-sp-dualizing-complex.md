+++
id = "det-sp-dualizing-complex"
kind = "definition"
title = "The relative dualizing complex: data and well-definedness"
uses = ["det-sf-existence-brown", "det-sf-mate-open-restriction", "sk-def-sfb-dc-upper-shriek", "sk-prop-sp-et-proet"]
+++
Let $\Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\Qlb\}$ be admissible and let $f:X\to Y$
be a smooth separated morphism of finite type between standing schemes, of
pure relative dimension $d$. The data are:

1. the constant coefficient object $\Lambda_Y\in\Dctf(Y,\Lambda)$ (the
coefficient sheaf pulled back from the condensed ring $\Lambda$, placed in
degree $0$);
2. the exceptional inverse image
$f^!_\Lambda:\Loc(\Dctf(Y,\Lambda))\to\Loc(\Dctf(X,\Lambda))$, the right adjoint of
$Rf_{!,\Lambda}$ given by Brown representability ([det-sf-existence-brown]),
together with its counit $\varepsilon:Rf_{!,\Lambda}f^!_\Lambda\to\mathrm{id}$.

The *relative dualizing complex* is the object
$\omega_{f,\Lambda}=f^!_\Lambda\Lambda_Y$, together with the counit
$\varepsilon_{\Lambda_Y}:Rf_{!,\Lambda}\omega_{f,\Lambda}\to\Lambda_Y$. It is well
defined:

- $\Lambda_Y$ lies in $\Dctf(Y,\Lambda)$: it is constructible (constant on the
single stratum $Y$) and of Tor amplitude $[0,0]$ (for $\mathcal O_E$, $E$ and
$\Qlb$, $\Dctf=\Dbc$ and only constructibility is required);
- $\omega_{f,\Lambda}$ lies in $\Dctf(X,\Lambda)$ because $f^!_\Lambda$ carries
$\Dctf(Y,\Lambda)$ into $\Dctf(X,\Lambda)$ (the restriction theorem recorded in
[sk-def-sfb-dc-upper-shriek]);
- the pair $(\omega_{f,\Lambda},\varepsilon_{\Lambda_Y})$ is unique up to unique
isomorphism: it represents the functor
$M\mapsto\Hom(Rf_{!,\Lambda}M,\Lambda_Y)$ on $\Loc(\Dctf(X,\Lambda))$, so by the
Yoneda lemma it is independent of the choice of right adjoint and of the
compactification used to define $Rf_{!,\Lambda}$;
- for an open immersion $u:U\to X$ there is a canonical
isomorphism $u^*\omega_{f,\Lambda}\simeq\omega_{fu,\Lambda}$
([det-sf-mate-open-restriction]), so $\omega_{f,\Lambda}$ is compatible with
restriction to opens of $X$.

With finite coefficients $A$ the same object may be formed on the étale site,
$\omega^{\mathrm{ét}}_{f,A}=f^!A_Y$ in $\Dctf(X_{\mathrm{ét}},A)$, and the comparison
$\nu_X^*$ carries it to $\omega_{f,A}$ ([sk-prop-sp-et-proet]).
