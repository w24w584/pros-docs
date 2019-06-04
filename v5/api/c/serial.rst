.. highlight:: c
   :linenothreshold: 5

=====================================
Smart Port Serial Communication C API
=====================================

.. note:: Additional example code for this module can be found in
          `its Tutorial <../../tutorials/topical/serial.html>`_.

.. contents:: :local:

Functions
=========

serial_enable
-------------

Enables generic serial on the given port.

.. note::
   This function must be called before any of the generic serial functions will work.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port

Analogous to `pros::Serial::enable <../cpp/serial.html#enable>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_enable ( uint8_t port )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
============ ===================================================================

**Returns:** 1 if the operation was successful or ``PROS_ERR`` if the operation failed, setting ``errno``.

----

serial_set_baudrate
-------------------

Sets the baudrate for the serial port to operate at.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port

Analogous to `pros::Serial::set_baudrate <../cpp/serial.html#set-baudrate>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_set_baudrate ( uint8_t port,
                                      int32_t baudrate )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          serial_set_baudrate(GENERIC_COMM_PORT, 115200);
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
 baudrate     The baudrate to operate at
============ ===================================================================

**Returns:** 1 if the operation was successful or ``PROS_ERR`` if the operation failed, setting ``errno``.

----

serial_flush
------------

Clears the internal input and output FIFO buffers.

This can be useful to reset state and remove old, potentially unneeded data
from the input FIFO buffer or to cancel sending any data in the output FIFO
buffer.

.. note::
   This function does not cause the data in the output buffer to be
   written, it simply clears the internal buffers. Unlike stdout, generic
   serial does not use buffered IO (the FIFO buffers are written as soon
   as possible).

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port

Analogous to `pros::Serial::flush <../cpp/serial.html#flush>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_flush ( uint8_t port )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          serial_flush(GENERIC_COMM_PORT);
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
============ ===================================================================

**Returns:** 1 if the operation was successful or ``PROS_ERR`` if the operation failed, setting ``errno``.

----

serial_get_read_avail
---------------------

Returns the number of bytes available to be read in the the port's FIFO
input buffer.

.. note::
   This function does not actually read any bytes, is simply returns the
   number of bytes available to be read.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port

Analogous to `pros::Serial::get_read_avail <../cpp/serial.html#get-read-avail>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_get_read_avail ( uint8_t port )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          printf("Available bytes to read: %d\n", serial_get_read_avail(GENERIC_COMM_PORT));
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
============ ===================================================================

**Returns:** The number of bytes avaliable to be read or PROS_ERR if the operation failed, setting errno.

----

serial_get_write_free
---------------------

Returns the number of bytes free in the port's FIFO output buffer.

.. note::
   This function does not actually write any bytes, is simply returns the
   number of bytes free in the port's buffer.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port

Analogous to `pros::Serial::get_write_free <../cpp/serial.html#get-write-free>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_get_write_free ( uint8_t port )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          printf("Available bytes to write: %d\n", serial_get_write_free(GENERIC_COMM_PORT));
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
============ ===================================================================

**Returns:** The number of bytes free or PROS_ERR if the operation failed,
setting errno.

----

serial_peek_byte
----------------

Reads the next byte avaliable in the port's input buffer without removing it.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port

Analogous to `pros::Serial::peek_byte <../cpp/serial.html#peek_byte>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_peek_byte ( uint8_t port )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          printf("Next byte available: %d\n", serial_peek_byte(GENERIC_COMM_PORT));
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
============ ===================================================================

**Returns:** The next byte avaliable to be read, -1 if none are available, or
PROS_ERR if the operation failed, setting errno.

----

serial_read_byte
----------------

Reads the next byte available in the port's input buffer.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port

Analogous to `pros::Serial::read_byte <../cpp/serial.html#read_byte>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_read_byte ( uint8_t port )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          printf("Next byte available: %d\n", serial_read_byte(GENERIC_COMM_PORT));
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
============ ===================================================================

**Returns:** The next byte avaliable to be read, -1 if none are available, or
PROS_ERR if the operation failed, setting errno.

----

serial_read
-----------

Reads up to the next length bytes from the port's input buffer and places
them in the user supplied buffer.

.. note::
   This function will only return bytes that are currently available to be
   read and will not block waiting for any to arrive.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port

Analogous to `pros::Serial::read <../cpp/serial.html#read>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_read ( uint8_t port,
                              uint8_t* buffer,
                              int32_t length )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          char[10] buf;
          serial_read(GENERIC_COMM_PORT, buf, sizeof(buf));
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
 buffer       The location to put the data read
 length       The maximum number of bytes to read
============ ===================================================================

**Returns:** The number of bytes read or PROS_ERR if the operation failed, setting errno.

----

serial_write_byte
-----------------

Write the given byte to the port's output buffer.

.. note::
   Data in the port's output buffer is written to the serial port as soon
   as possible on a FIFO basis and can not be done manually by the user.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port
- ``EIO`` - Serious internal write error.

Analogous to `pros::Serial::write_byte <../cpp/serial.html#write_byte>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_write_byte ( uint8_t port,
                                    uint8_t buffer )

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          char to_write = 0x80;
          serial_write_byte(GENERIC_COMM_PORT, to_write);
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
 buffer       The byte to write
============ ===================================================================

**Returns:** The number of bytes written or PROS_ERR if the operation failed,
setting errno.

----

serial_write_byte
-----------------

Writes up to length bytes from the user supplied buffer to the port's output
buffer.

.. note::
   Data in the port's output buffer is written to the serial port as soon
   as possible on a FIFO basis and can not be done manually by the user.

This function uses the following values of ``errno`` when an error state is reached:

- ``EINVAL``  - The given value is not within the range of V5 ports (1-21)
- ``EACCES`` - Another resource is currently trying to access the port
- ``EIO`` - Serious internal write error.

Analogous to `pros::Serial::write <../cpp/serial.html#write>`_.

.. tabs ::
   .. tab :: Prototype
      .. highlight:: c
      ::

        int32_t serial_write ( uint8_t port,
                               uint8_t* buffer,
                               int32_t length)

   .. tab :: Example
      .. highlight:: c
      ::

        #define GENERIC_COMM_PORT 1

        void initialize() {
          serial_enable(GENERIC_COMM_PORT);
          char[10] buf;
          char to_write = 0x80;
          buf[0] = to_write;
          serial_write(GENERIC_COMM_PORT, buf, sizeof(buf));
        }

============ ===================================================================
 Parameters
============ ===================================================================
 port         The V5 port number from 1-21
 buffer       The data to write
 length       The maximum number of bytes to write
============ ===================================================================

**Returns:** The number of bytes written or PROS_ERR if the operation failed,
setting errno.

----
