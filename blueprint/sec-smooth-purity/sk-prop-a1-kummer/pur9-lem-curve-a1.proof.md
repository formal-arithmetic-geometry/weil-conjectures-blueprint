+++
kind = "proof"
of = "pur9-lem-curve-a1"
uses = ["pur9-lem-roots-constant"]
+++
$\Aaf^1_k$ is connected, so global sections of a constant sheaf are $M$. For $q\geq2$, -prop-cd-affineZZ gives vanishing, $\Aaf^1_k$ being an affine curve. For $q=1$, $M$ has a composition series with quotients $\mathbf Z/\ell$, and the long exact sequences (with $H^0$ exact on constant sheaves of a connected scheme and $H^2=0$) reduce to $M=\mathbf Z/\ell\cong\mu_\ell(k)$ (Lemma [pur9-lem-roots-constant]). The Kummer sequence (-prop-kummer-exactZZ) and Hilbert 90 (-prop-hilbert90ZZ) give the exact sequence $\Gamma(\mathbb G_m)\xrightarrow{\ell}\Gamma(\mathbb G_m)\to H^1(\Aaf^1_k,\mu_\ell)\to\Pic(\Aaf^1_k)$. Here $\Gamma(\Aaf^1_k,\mathbb G_m)=k[T]^\times=k^\times$ is $\ell$-divisible, $k$ being algebraically closed, and $\Pic(\Aaf^1_k)=0$ because $k[T]$ is a principal ideal domain. Hence $H^1=0$.
