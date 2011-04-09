"""The application's model objects"""
from wishdex.model.meta import Session, Base

from sqlalchemy import orm, Table, Column, ForeignKey, Index, PrimaryKeyConstraint, ForeignKeyConstraint, UniqueConstraint, schema

from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, INTEGER, SMALLINT, TINYINT, CHAR, VARCHAR, DATE, DATETIME, BOOLEAN, BINARY, BLOB, TEXT, DOUBLE, VARBINARY, MEDIUMINT

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

user = Table('user', Base.metadata,
    Column('user_id', INTEGER(unsigned=True), primary_key=True),
    Column('user_password', BINARY(128), index=True),
    Column('user_first_name', VARCHAR(64)),
    Column('user_last_name', VARCHAR(64)),
    Column('user_profile', BLOB),
    Column('user_fb_id', BIGINT(unsigned=True), index=True),
    Column('user_username', VARCHAR(64), index=True),
    Column('user_email', VARCHAR(128)), ## Index on this
    Column('user_has_image', TINYINT(unsigned=True)),
    Column('user_join_date', DATETIME),
)

wishdex = Table('wishdex', Base.metadata,
    Column('wishdex_id', INTEGER(unsigned=True), primary_key=True),
    Column('wishdex_user_id', INTEGER(unsigned=True), ForeignKey('user.user_id'), index=True),
    Column('wishdex_name', VARCHAR(64)),
)
 
item = Table('item', Base.metadata,
    Column('item_id', INTEGER(unsigned=True), primary_key=True),
    Column('item_wishdex_id', INTEGER(unsigned=True), ForeignKey('wishdex.wishdex_id'), index=True),
    Column('item_name', VARCHAR(100)),
    Column('item_price', INTEGER(unsigned=True)),
    Column('item_link', BLOB),
)

favorite = Table('favorite', Base.metadata,
    Column('favorite_id', INTEGER(unsigned=True), primary_key=True),
    Column('favorite_user_id', INTEGER(unsigned=True), ForeignKey('user.user_id'), index=True),
    Column('favorite_item_id', INTEGER(unsigned=True), ForeignKey('item.item_id'), index=True),
    Column('favorite_time', DATETIME),
)
