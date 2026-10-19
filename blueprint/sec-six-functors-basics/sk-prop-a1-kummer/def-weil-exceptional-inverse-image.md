+++
id = "def-weil-exceptional-inverse-image"
kind = "definition"
title = "Exceptional inverse image notation"
order = 1848
uses = ["def-compact-support-direct-image-detailed", "def-weil-ambient-exceptional-adjoint", "def-weil-exceptional-adjoint-admissibility", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "sk-thm-existence", "sk-def-sfb-dc-upper-shriek", "sk-prop-scalar-six"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$ with valuation ring $\mathcal
O_E$ and uniformizer $\pi_E$, and an integer $n\in\mathbf Z_{\geq1}$, with
$A=A_{E,n}=\mathcal O_E/\pi_E^n$. Let $S$ be a scheme on which $\ell$ is
invertible, let $X,Y$ be finite-type
[def-weil-scheme-morphism-properties] $S$-schemes, and let $f:X\to Y$ be a
separated finite-type $S$-morphism; in every use $S=\Spec k$
with $k$ a field, so that $X$ and $Y$ are Noetherian. Let
$f^{\times}:D(Y_{\mathrm{et}},A)\to D(X_{\mathrm{et}},A)$ be the
right adjoint of the etale compact-support functor
$Rf^{\mathrm{et}}_!=Rp_{\mathrm{et},*}j^{\mathrm{et}}_!$ attached to a
compactification, on the ordinary etale derived categories of the Noetherian
schemes $X,Y$; it exists by Brown representability. Use finite-torsion constructibility
[def-weil-finite-torsion-constructibility] and the compact-support direct image
[def-compact-support-direct-image-detailed]. On the small pro-etale sites
[def-weil-pbc-proetale-site], with $\nu_X,\nu_Y$ the comparison morphisms
[def-weil-pbc-site-comparison-morphism], *define*

$$
 Rf_n^!:=\nu_X^*\,f^{\times}\,R\nu_{Y,*}:
 D^+(Y_{\mathrm{proet}},A_{E,n})\longrightarrow D^+(X_{\mathrm{proet}},A_{E,n}),
$$

the etale right adjoint transported along the etale/pro-etale comparison;
on $D^b_c(Y,A_{E,n})$, every object of which is of etale origin,
$L\cong\nu_Y^*G$, this is $Rf_n^!L=\nu_X^*f^{\times}G$, and one restricts to

$$
 Rf_n^!:D^b_c(Y,A_{E,n})\longrightarrow D^b_c(X,A_{E,n}).
$$

For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$, regarded as condensed rings, $Rf^!$ is
not built from the finite levels. By [sk-thm-existence] (3), a single
application of Brown representability gives an exact right adjoint $f^!$ of
$Rf_!$ on $\Loc(\Dctf(-,\Lambda))$, and by [sk-thm-existence] (4) it carries
$\Dctf(Y,\Lambda)$ into $\Dctf(X,\Lambda)$. Since $\Dctf=\Dbc$ for these
coefficients, this restriction is a functor

$$
 Rf^!:D^b_c(Y,\Lambda)\longrightarrow D^b_c(X,\Lambda)
$$

on the condensed bounded constructible categories; by uniqueness of adjoints
it agrees with $i^*\circ Rp^!$ of [sk-def-sfb-dc-upper-shriek] for a
compactification $f=p\circ i$. Its compatibility with reduction
$\mathcal O_E\to A_{E,n}$, localization $\mathcal O_E\to E$ and extension of
scalars $E\to F\to\Qlb$ is a consequence ([sk-prop-scalar-six]), not part of
the definition.

For $K\in D^b_c(X,\Lambda)$ and $L\in D^b_c(Y,\Lambda)$, characterize the
resulting functors, at every $\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, by the
natural adjunction isomorphisms

$$
 \Hom_Y(Rf_!K,L)\cong\Hom_X(K,Rf^!L).
$$

The two defining properties of the finite-level functor $Rf_n^!$ are theorems,
not hypotheses.
The adjunction isomorphism holds for every bounded-below $K$ of etale origin
(in particular every $K\in D^b_c(X,A_{E,n})$) and every bounded-below $L$,
with units and counits compatible with refinements of the compactification
(the etale adjunction transported by the compact-support comparison and the
full faithfulness of $\nu^*$ on $D^+$). The displayed typing — that $Rf_n^!$
carries $D^b_c(Y,A_{E,n})$ into $D^b_c(X,A_{E,n})$, and finite-Tor objects
[def-weil-finite-tor-amplitude] into finite-Tor objects, with explicit bounds
$[a,b]\mapsto[a-2D,b+2\dim Y+1]$ independent of $n$, where $D$ is the maximal
embedding dimension of the affine charts $U\hookrightarrow\mathbf A^{d_U}_V$ of $f$ — is proved by localizing
on affine charts and composing the closed-immersion and smooth cases. These
are the analogues, for the constructible functor, of clauses (2) and (3) of
[def-weil-exceptional-adjoint-admissibility].

The ambient exceptional right adjoint datum
[def-weil-ambient-exceptional-adjoint] is *not* assumed in this definition,
and it is false in general: for the structure morphism of an elliptic curve
over $\overline{\mathbf F}_p$ with $A=\mathbf F_r$ the functor $Rf_*=Rf_!$ has
no right adjoint on $D(X_{\mathrm{proet}},A)$, nor on $D^+$. When the datum
holds together with the preservation clauses of
[def-weil-exceptional-adjoint-admissibility], the restriction of the ambient
$Rf_n^{\times}$ to $D^b_c(Y,A_{E,n})$ agrees with $Rf_n^!$ by uniqueness of
adjoints.
