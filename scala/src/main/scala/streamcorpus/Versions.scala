/**
 * generated by Scrooge 3.0.7-SNAPSHOT
 */
package streamcorpus

import com.twitter.scrooge.ThriftEnum

/**
 * Versions of this protocol are enumerated so that when we expand,
 * everybody can see which version a particular data file used.
 *
 * v0_1_0 refers to the kba.thrift definition, which was before
 * Versions was included in the spec.
 */
case object Versions {
  case object V020 extends Versions {
    val value = 0
    val name = "V020"
  }

  /**
   * Find the enum by its integer value, as defined in the Thrift IDL.
   * @throws NoSuchElementException if the value is not found.
   */
  def apply(value: Int): Versions = {
    value match {
      case 0 => V020
      case _ => throw new NoSuchElementException(value.toString)
    }
  }

  /**
   * Find the enum by its integer value, as defined in the Thrift IDL.
   * Returns None if the value is not found
   */
  def get(value: Int): Option[Versions] = {
    value match {
      case 0 => scala.Some(V020)
      case _ => scala.None
    }
  }

  def valueOf(name: String): Option[Versions] = {
    name.toLowerCase match {
      case "v020" => scala.Some(Versions.V020)
      case _ => scala.None
    }
  }
}


/**
 * Versions of this protocol are enumerated so that when we expand,
 * everybody can see which version a particular data file used.
 *
 * v0_1_0 refers to the kba.thrift definition, which was before
 * Versions was included in the spec.
 */
sealed trait Versions extends ThriftEnum with Serializable