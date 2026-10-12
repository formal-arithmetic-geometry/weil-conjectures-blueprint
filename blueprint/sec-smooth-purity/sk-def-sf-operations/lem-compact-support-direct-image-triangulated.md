+++
id = "lem-compact-support-direct-image-triangulated"
kind = "lemma"
title = "Triangulatedness of the finite-level compact-support direct image"
order = 1848
uses = ["def-compact-support-direct-image-detailed", "def-weil-compact-support-candidate", "def-weil-compactifications-refinements", "def-weil-derived-direct-image", "def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "lem-weil-extension-by-zero-exact"]
+++
Let $K_0$ be a field, let $X,Y$ be finite-type
[def-weil-scheme-morphism-properties] $K_0$-schemes, and let $f:X\to Y$ be a
separated finite-type $K_0$-morphism. Fix a prime $\ell$, write
$\Ql=\mathbf Q_\ell$, and require that its image in $K_0$ is invertible.
Choose a finite extension $E/\Ql$, an integer $n\in\mathbf Z_{\geq1}$, and
put $A=A_{E,n}$. For every object $c\in\operatorname{Comp}(f)$ of the
compactification category [def-weil-compactifications-refinements], the
functor

$$
 Rf_{!,n}=Rf_{!,n}^{c}:
 D(X_{\mathrm{proet}},A_{E,n})\longrightarrow D(Y_{\mathrm{proet}},A_{E,n})
$$

of [def-compact-support-direct-image-detailed] is a triangulated functor: it
preserves shifts and carries distinguished triangles to distinguished
triangles.
