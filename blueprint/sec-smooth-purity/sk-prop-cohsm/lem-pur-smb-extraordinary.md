+++
id = "lem-pur-smb-extraordinary"
kind = "lemma"
title = "Smooth base change for the exceptional inverse image"
order = 2335
uses = ["cor-sf-ambient-adjoint-discharge", "def-exchange-projection", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-ambient-exceptional-adjoint", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "prop-asd-smooth-base-change", "thm-cbc-finite-level-proetale", "thm-sf-ambient-adjoint-class", "thm-weil-pbc-site-comparison"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let

$$
\begin{array}{ccc}
X'&\xrightarrow{\ u\ }&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{\ v\ }&Y
\end{array}
$$

be a Cartesian square in which $f$ is
smooth of pure relative dimension
$d$; the
ambient exceptional right
adjoint datum of [def-weil-ambient-exceptional-adjoint] is not assumed,
the right adjoints $Rf^!$, $Rf'^!$ that occur being, on the coefficients
used here, the theorem [cor-sf-ambient-adjoint-discharge]. Let
$K\in D^b_{ctf}(Y,\Lambda)$. The canonical
comparison

$$
Lu^*Rf^!K\xrightarrow{\ \sim\ }Rf'^!Lv^*K
$$

is an isomorphism. The morphism $v$ is arbitrary; its base change
$f'$ is smooth of the same relative dimension.
