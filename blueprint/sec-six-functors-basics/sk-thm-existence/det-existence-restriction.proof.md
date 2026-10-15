+++
kind = "proof"
of   = "det-existence-restriction"
uses = ["sk-prop-sf-rf-shriek-preservation", "sk-thm-restriction", "sk-thm-int-restriction", "sk-prop-int-brown"]
+++
As in [det-existence-localizing] it suffices to treat $A$, $\cO_E$, $E$ and $\Qlb$; in each case
$f^!$ is the right adjoint of [det-existence-localizing] (3).

- For a finite ring $A$ the inclusion $f^!(\Dctf(Y,A))\subseteq\Dctf(X,A)$ is
  [sk-prop-sf-rf-shriek-preservation].
- For $\Lambda=E$ or $\Qlb$ it is [sk-thm-restriction].
- For $\Lambda=\cO_E$ the right adjoint of [sk-prop-int-brown] is the same functor, and the
  inclusion is [sk-thm-int-restriction].

Given the inclusion, the restriction of the adjunction is formal: $Rf_!$ maps $\Dctf(X,\Lambda)$
into $\Dctf(Y,\Lambda)$ by [det-existence-localizing] (2), and for $M\in\Dctf(X,\Lambda)$ and
$N\in\Dctf(Y,\Lambda)$ the bijection $\Hom(Rf_!M,N)\simeq\Hom(M,f^!N)$ is computed in the full
subcategories $\Dctf$.
